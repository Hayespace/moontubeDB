import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
@app.route("/get_videos")
def get_videos():
    videos = mongo.db.videos.find()
    return render_template("videos.html", videos=videos, show_buttons=False)

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
        # Check if username already exists in db
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

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile"))

    return render_template("register.html")

# User login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("profile"))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# User profile with uploaded videos
@app.route("/profile")
def profile():
    if "user" in session:
        username = session["user"]
        user_uploaded_videos = list(mongo.db.videos.find({"created_by": username}))
        return render_template("profile.html", username=username, user_uploaded_videos=user_uploaded_videos)
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
        return redirect(url_for("get_videos"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_video.html", categories=categories)

# Edit a video
@app.route("/edit_video/<video_id>", methods=["GET", "POST"])
def edit_video(video_id):
    if request.method == "POST":
        hire_me = "hire" if request.form.get("hire_me") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "video_title": request.form.get("video_title"),
            "video_description": request.form.get("video_description"),
            "hire_me": hire_me,
            "video_link": request.form.get("video_link"),
            "created_by": session["user"]
        }
        mongo.db.videos.update_one({"_id": ObjectId(video_id)}, {"$set": submit})
        flash("Video Successfully Updated")

    video = mongo.db.videos.find_one({"_id": ObjectId(video_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_video.html", video=video, categories=categories)

# Delete a video
@app.route("/delete_video/<video_id>")
def delete_video(video_id):
    mongo.db.videos.delete_one({"_id": ObjectId(video_id)})
    flash("Video Successfully Deleted")
    return redirect(url_for("get_videos"))

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

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
