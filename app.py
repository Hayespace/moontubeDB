import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Main route to display videos
@app.route("/")
def get_videos():
    categories = mongo.db.categories.find().sort("category_name", 1)
    categorized_videos = {}

    for category in categories:
        category_name = category["category_name"]
        videos = list(mongo.db.videos.find({"category_name": category_name}))
        categorized_videos[category_name] = videos

    # Retrieve "featured" videos
    featured_videos = list(mongo.db.videos.find({"category_name": "Featured"}))

    return render_template("videos.html", categorized_videos=categorized_videos, featured_videos=featured_videos, show_buttons=False)


# Search route
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    videos = list(mongo.db.videos.find({"$text": {"$search": query}}))
    return render_template("videos.html", videos=videos, show_buttons=False)


# User registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile"))

    return render_template("register.html")

# User login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("profile"))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# User profile with uploaded videos
@app.route("/profile")
def profile():
    if "user" in session:
        username = session["user"]
        user_uploaded_videos = list(mongo.db.videos.find({"created_by": username}))
        
        if username == "admin":
            # If the user is admin, get all videos
            all_videos = list(mongo.db.videos.find())
            return render_template("profile.html", username=username, user_uploaded_videos=user_uploaded_videos, all_videos=all_videos, show_buttons=True)
        else:
            return render_template("profile.html", username=username, user_uploaded_videos=user_uploaded_videos, show_buttons=True)
    else:
        return redirect(url_for("login"))


# User logout
@app.route("/logout")
def logout():
    # Remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add a new video
@app.route("/add_video", methods=["GET", "POST"])
def add_video():
    if request.method == "POST":
        hire_me = "hire" if request.form.get("hire_me") else "off"
        video = {
            "category_name": request.form.get("category_name"),
            "video_title": request.form.get("video_title"),
            "video_description": request.form.get("video_description"),
            "hire_me": hire_me,
            "video_link": request.form.get("video_link"),
            "created_by": session["user"]
        }
        mongo.db.videos.insert_one(video)
        flash("Video Successfully Added")
        
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_video.html", categories=categories)


@app.route("/edit_video/<video_id>", methods=["GET", "POST"])
def edit_video(video_id):
    if request.method == "POST":
        category_name = request.form.get("category_name")
        video_title = request.form.get("video_title")
        video_description = request.form.get("video_description")
        hire_me = request.form.get("hire_me") if request.form.get("hire_me") else "off"
        video_link = request.form.get("video_link")

        video_data = {
            "category_name": category_name,
            "video_title": video_title,
            "video_description": video_description,
            "hire_me": hire_me,
            "video_link": video_link
        }

        mongo.db.videos.update_one({"_id": ObjectId(video_id)}, {"$set": video_data})
        flash("Video Successfully Updated")
        return redirect(url_for("get_categories"))

    video = mongo.db.videos.find_one({"_id": ObjectId(video_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_video.html", video=video, categories=categories)


# Delete a video
@app.route("/delete_video/<video_id>")
def delete_video(video_id):
    mongo.db.videos.delete_one({"_id": ObjectId(video_id)})
    flash("Video Successfully Deleted")
    return redirect(url_for("get_categories"))


# Get all categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Add a new category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Edit a category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, {"$set": submit})
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete a category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# Edit Profile
@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "user" in session:
        username = session["user"]
        user = mongo.db.users.find_one({"username": username})

        if request.method == "POST":
            new_username = request.form.get("username")
            new_email = request.form.get("email")
            about_me = request.form.get("about_me")
            selected_animal = request.form.get("selected_animal")

            user_data = {
                "username": new_username,
                "email": new_email,
                "about_me": about_me,
                "selected_animal": selected_animal
            }

            mongo.db.users.update_one({"username": username}, {"$set": user_data})
            flash("Profile updated successfully!")
            return redirect(url_for("profile"))

        return render_template("edit_profile.html", current_user=user)
    else:
        return redirect(url_for("login"))


# Moontuber Profile
@app.route('/moontuber_profile/<username>')
def moontuber_profile(username):
    user = mongo.db.users.find_one({"username": username})
    user_uploaded_videos = list(mongo.db.videos.find({"created_by": username}))
    selected_animal = user.get("selected_animal")

    return render_template('moontuber_profile.html', user=user, user_uploaded_videos=user_uploaded_videos, selected_animal=selected_animal)


# Moontuber Directory
@app.route("/moontuber_dir")
def moontuber_directory():
    pipeline = [
        {
            "$lookup": {
                "from": "videos",
                "localField": "username",
                "foreignField": "created_by",
                "as": "user_videos"
            }
        }
    ]

    users = mongo.db.users.aggregate(pipeline)

    return render_template("moontuber_dir.html", users=users)

# Admin Users
@app.route("/users")
def list_users():
    if "user" in session:
        if session["user"] == "admin":
            users = list(mongo.db.users.find())
            return render_template("users.html", users=users)
    return redirect(url_for("login"))


# Delete a user
@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    if "user" in session and session["user"] == "admin":
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        flash("User Successfully Deleted")
        return redirect(url_for("list_users"))
    return redirect(url_for("login"))


# Retrieve all videos from MongoDB
@app.route("/admin_videos")
def admin_videos():
    if "user" in session and session["user"] == "admin":
        videos = list(mongo.db.videos.find())
        return render_template("admin_videos.html", videos=videos)
    return redirect(url_for("login"))

    
# Video Selected and Comments
@app.route("/video_detail/<video_id>")
def video_detail(video_id):
    video = mongo.db.videos.find_one({"_id": ObjectId(video_id)})
    if video:
        # Fetch comments related to this video
        video_comments = list(mongo.db.comments.find({"video_id": video_id}))
        return render_template("video_detail.html", video=video, video_comments=video_comments)
        return render_template("video_detail.html", video=video, video_comments=video_comments, current_user=session.get("user"))
    else:
        flash("Video not found")
        return redirect(url_for("get_videos"))

# Comments Section
@app.route("/submit_comment/<video_id>", methods=["POST"])
def submit_comment(video_id):
    if "user" in session:
        username = session["user"]
        comment_text = request.form.get("comment")
        video = mongo.db.videos.find_one({"_id": ObjectId(video_id)})

        if video:
            # Create a comment document
            comment = {
                "user": username,
                "text": comment_text,
                "video_id": video_id
            }
            mongo.db.comments.insert_one(comment)
            flash("Comment added successfully!", "success")
        else:
            flash("Video not found", "error")

    return redirect(url_for("video_detail", video_id=video_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
