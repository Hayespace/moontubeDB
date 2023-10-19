# Moontube: A Crypto Streaming Platform

![responsiveness](/static/assets/responsiveness.png)

**Visit MOONTUBE at [Moontube](https://moontube-db-1e90f4bf79ae.herokuapp.com/)**

Welcome to MOONTUBE, the platform for connecting investors, crypto developers, and YouTubers all in one place. MOONTUBE streamlines the crypto community by providing a secure space to find influencers, create marketing opportunities, and promote projects. MOONTUBE simplifies the crypto experience with just a click.

To access the admin specific features please use the following details:

**Username:** admin

**Password:** 123456

## Table of Contents
1. [User Stories](#user-stories)
2. [Design and Color Scheme](#design-and-color-scheme)
3. [Features](#features)
4. [Wireframe](#wireframe)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Database](#data-schema)
8. [Unfixed Bugs](#unfixed-bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)

## Moontube User Stories

In the world of cryptocurrency, the term "moon" is a popular slang term used by enthusiasts and traders. It refers to a significant and often rapid increase in the price of a cryptocurrency, resulting in substantial profits for those who hold the asset. When a cryptocurrency is said to be "mooning," it means that its value is soaring to new heights, reaching a point where the investors who believed in it early on are reaping substantial financial rewards. The use of "moon" in cryptocurrency is closely tied to the idea of reaching the moon, a metaphor for achieving great financial success through investments.

The relevance of the name MOONTUBE for a streaming platform in the crypto space is multi-fold:

- **Positive Connotation:** The term "moon" in the context of cryptocurrency is associated with optimism and profit. It represents the ultimate goal for many crypto investors - seeing their investments skyrocket in value. By incorporating "moon" into the name, MOONTUBE aligns itself with this positive and ambitious sentiment.

- **Community Engagement:** Cryptocurrency communities often use the concept of "moon" to create excitement and engagement. MOONTUBE, as a streaming platform, can tap into this enthusiasm by providing a space for enthusiasts to share their experiences, insights, and knowledge, further fueling the ambition to reach the moon.

"Moon" in the context of cryptocurrency symbolizes the dream of financial success and prosperity. MOONTUBE's name captures this spirit and invites users to be part of a community and platform that embraces the excitement and ambition of the crypto space.

MOONTUBE users will:

**Easily Connect with Influencers:** MOONTUBE simplifies the process of connecting with influencers and exploring marketing opportunities for token developers, aligning with the optimistic and profit-driven sentiment associated with "moon" in crypto. Users can hire Moontubers for their expertise in promoting cryptocurrency projects and products.

**Build a Strong Community:** MOONTUBE serves as a hub for like-minded individuals, fostering connections and discussions within a single platform. It's not just about financial gains but also about the crypto lifestyle, technology, and culture that surrounds it. Users can engage in discussions and collaborate on cryptocurrency-related projects, bringing the community closer to achieving their financial goals.

**For YouTubers, Developers, and Investors:** Whether you're a YouTuber seeking collaboration, a developer looking for secure promotion opportunities, or an investor aiming to ride the wave of a "moon" project, MOONTUBE enables users to explore the limitless potential of the crypto world. Content creators can add and edit videos, interact with their audience through comments, and indicate their availability for hire. Token developers and investors can easily find experts and influencers who can help them reach new heights in the crypto market.


## Design and Color Scheme

The MOONTUBE visual aesthetic is a reflection of the universe of cryptocurrencies. I have drawn inspiration from the moon and space, infusing the platform with a celestial vibe.

![logo](/static/assets/logo2.png)

### Space-Inspired
Cryptocurrency, like the vastness of space, is full of possibilities. I have harnessed this inspiration to create a design that evokes the mystery and excitement of the crypto world. From the logo to the spacey hues that enhance the overall experience.

### Sleek and Dark
The scheme is designed to be sleek, like the black canvas of outer space. The dark background provides a comfortable and immersive viewing experience.

![Featured](/static/assets/featured_carousel.png)

### Solar Flares and Lens Flares
Incorporating elements inspired by solar flares and lens flares adds dynamic energy to the design.

![background](/static/assets/flare2.png)

The design and color scheme aim to make your journey through the crypto universe not only informative but also visually captivating. MOONTUBE is more than just a platform; it's an experience that immerses you in the cosmic realm of cryptocurrency.

### Landing Page Design

The Moontube landing page is carefully designed to create an immersive and user-friendly experience for visitors. Here's an overview of the key design elements:

1. **Crypto-Themed Videos**
The heart of Moontube's landing page is its collection of crypto-themed videos, prominently displayed in the central area. These videos are organized into various categories, making it easy for users to discover content that interests them. The categories can cover a wide range of crypto-related topics, from blockchain technology and cryptocurrency tutorials to market analysis and investment strategies.

2. **Features Carousel**
At the top of the landing page is an interactive features carousel. This section is designed to showcase the platform's most exciting features and highlight content curated by the admin user. The admin can easily update this carousel, ensuring that the most relevant and engaging content is always in the spotlight.

3. **Sleek Logo and Branding**
On the left-hand panel of the landing page, users are greeted by Moontube's sleek and visually appealing logo. The logo encapsulates the essence of crypto-space, reflecting the platform's unique aesthetic.

4. **User Information and Search Bar**
Beneath the logo is a minimalist panel that provides information about the site and a simple search bar.

5. **Simple Top Navigation**
Moontube's top navigation bar is designed to be clean and straightforward, focusing on user experience. It features only two words, "Home" and "Portal," making navigation intuitive. A dropdown menu in the top right corner provides access to additional features.

![Landing](/static/assets/landing.png)

## Features

MOONTUBE offers a comprehensive set of features that empower both regular users and administrators to make the most of the platform, whether it's for content creation, community engagement, or platform management.

### User Account
  - Registered users can create accounts on MOONTUBE.
  - They have the ability to create profiles and add YouTube video links with descriptions.
  - Users also have the option to indicate whether they can be hired for services, comment on other users' videos, and actively engage with the MOONTUBE community.
### Home Screen
![Login Screen](/static/assets/login_screen.png)
### Edit Profile
![Edit Profile](/static/assets/edit_prof.png)
### Hire Me 
![Hire](/static/assets/vid_hire.png)

### Add / Edit Video
- **Title:** MOONTUBE allows users to add or edit video titles.
- **Description:** Users can provide descriptions for their videos.
- **Link:** You can share your YouTube video link on MOONTUBE.
- **Category:** Categorize your videos for easier discovery.
- **For Hire Toggle:** MOONTUBE provides a 'For Hire' toggle switch to indicate your availability for work.
- **Red 'HIRE' Button:** Once selected, a red 'HIRE' button appears on the video card.
- **Profile Page Link:** If a user clicks the 'HIRE' button, they will be directed to the MOONTUBER's profile page for potential collaboration.

Once a video has been added the information is then commited to the database. The main landing page can then pull the information from the database and display the video in the correct categories;

    <h3>New Videos</h3>
    {% for category, videos in categorized_videos.items() %}
    {% if category != "Featured" %}
        <h4>
        <u>{{ category }}</u>
        </h4>
        <div class="row">
        {% for video in videos %}
            <div class="col s12 m6 l4 xl3">
            <div class="card card-style">
                <a href="{{ url_for('video_detail', video_id=video._id) }}">
                <h2>
                    <span class="card-title">{{ video.video_title }}</span>
                </h2>
                <div class="video-container">
                    <iframe src="{{ video.video_link }}?rel=0&modestbranding=1&controls=1&showinfo=0" title="video player" allowfullscreen></iframe>
                </div>
                <p>
                    <em>"{{ video.video_description }}"</em>
                </p>
                <p>
                    {% if video.hire_me == "hire" %}
                    <a href="{{ url_for('moontuber_profile', username=video.created_by) }}" class="btn-floating waves-effect waves-light red right">
                    <i class="material-icons tooltipped" data-position="bottom" data-tooltip="Hire Me!">{{ video.hire_me }}</i>
                    </a>
                    {% endif %}
                </p>
                <a href="{{ url_for('moontuber_profile', username=video.created_by) }}">
                    <p class="red-text">{{ video.created_by }}</p>
                </a>
                </a>
            </div>
            </div>
        {% endfor %}
        </div>
    {% endif %}
    {% endfor %}

### Add Video
![Add Video](/static/assets/addvid.png)
### Edit Video
![Add Video](/static/assets/editvid.png)

### Video Playback
  - MOONTUBE provides a responsive video player for smooth video streaming.
  - You have complete control over video playback, including volume adjustment and full-screen mode.
### Video
![Add Video](/static/assets/video_close.png)

### Embed Videos
MOONTUBE simplifies the video upload process and ensures that users can seamlessly share YouTube videos with the MOONTUBE community. The process for embedding videos involves converting the standard YouTube video URL into an embed format and displaying a video preview. Here's an overview of the process and the associated code that makes this feature work:

Process:

**User Input:** When users input a YouTube video URL into the designated field on MOONTUBE, the system checks if the URL is valid and supported for embedding.

**Validation:** The URL is validated to ensure it contains "youtube.com".

**Conversion to Embed Format:** If the URL is valid, the code extracts the unique video ID from the URL. It then converts the URL into an embed format that is compatible with displaying YouTube videos within the MOONTUBE platform.

**Video Preview:** After converting the URL, the code constructs an embedded YouTube iframe for the video with the specified video ID. This iframe is embedded within the MOONTUBE page, creating a video preview for users.

**Invalid URL Handling:** If the user enters an invalid or unsupported URL, MOONTUBE provides appropriate feedback, indicating that the URL is not suitable for embedding.

        // Function to convert a YouTube URL to the embed format
    function convertToEmbedUrl(url) {
        var videoId = getVideoIdFromUrl(url);
        if (videoId) {
            return 'https://www.youtube.com/embed/' + videoId;
        }
        return url;
    }

    // Function to extract the video ID from a YouTube URL
    function getVideoIdFromUrl(url) {
        var match = url.match(/[?&]v=([^&]+)/);
        return match ? match[1] : null;
    }


### Admin Features
  Administrators on MOONTUBE possess extensive capabilities beyond those of regular users. They have access to all the features available to regular users and can perform additional actions, including creating, updating, and deleting other users' videos and profiles. Additionally, admins can create new categories and curate the trending section, promoting content that deserves recognition within the MOONTUBE community

![Add Video](/static/assets/admonport.png)

**Code Examples for Admin Features**
1. **List Users (Admin Access Only)**
![Add Video](/static/assets/user_mgmt.png)

        # Admin Users
        @app.route("/users")
        def list_users():
            if "user" in session:
                if session["user"] == "admin":  # Check if the user is an admin
                    users = list(mongo.db.users.find())
                    return render_template("users.html", users=users)
            return redirect(url_for("login"))

    This code ensures that only users with the role "admin" can access the list of users. If the current user is not an admin, they are redirected to the login page.
    

2. **Delete User (Admin Access Only)**

        # Delete a user
        @app.route("/delete_user/<user_id>")
        def delete_user(user_id):
            if "user" in session and session["user"] == "admin":  # Check if the user is an admin
                mongo.db.users.delete_one({"_id": ObjectId(user_id)})
                flash("User Successfully Deleted")
                return redirect(url_for("list_users"))
            return redirect(url_for("login"))

    This code allows administrators to delete user accounts. Only users with the role "admin" can access this functionality.

3. **List Admin Videos (Admin Access Only)**
![Add Video](/static/assets/allvid_ad.png)

        # Retrieve all videos from MongoDB
        @app.route("/admin_videos")
        def admin_videos():
            if "user" in session and session["user"] == "admin":  # Check if the user is an admin
                videos = list(mongo.db.videos.find())
                return render_template("admin_videos.html", videos=videos)
            return redirect(url_for("login"))

    This route allows administrators to view all videos. Access is restricted to users with the role "admin."

4. **Navigation Bar Formatting (Admin Portal)**

![Add Video](/static/assets/dropdown_admin.png)

In your HTML navigation bar, you can control the visibility of the "Admin Portal" link based on the user's role:


        {% if session.user %}
        <li><a href="{{ url_for('add_video') }}">Add Video</a></li>
        <li><a href="{{ url_for('profile', username=session['user']) }}">Profile</a></li>
        {% if session.user|lower == "admin"|lower %}
            <li><a href="{{ url_for('get_categories') }}">Admin Portal</a></li>
        {% endif %}
        <li><a href="{{ url_for('logout') }}">Log Out</a></li>
        {% else %}
        <li><a href="{{ url_for('login') }}">Log In</a></li>
        <li><a href="{{ url_for('register') }}">Register</a></li>
        {% endif %}

The "Admin Portal" link is displayed only if the user's role, stored in the session, is "admin."

These code examples demonstrate how MOONTUBE implements admin-specific features with conditional formatting to restrict access to authorized administrators, enhancing the platform's management and curation capabilities.

### Hire Moontubers and Moontuber Profiles

- **Hire Moontubers**: MOONTUBE enables users to hire Moontubers for various services or collaborations. This feature can be accessed from the video page by clicking the "Hire" button or from the navigation bar's "Hire a Moontuber" option. This will direct them to either moontubers profile or to a directory of moontuber profiles.

- **Moontuber Directory**
![Directory](/static/assets/direct.png)

- **Moontuber Profiles**: Moontuber profiles contain information about the user. Users can view a Moontuber's bio, email address, and a list of videos created by that user. 
![Profile](/static/assets/profilepage.png)

### Comments
- Users can actively engage with the content by leaving comments below the videos. This feature fosters interaction and feedback within the MOONTUBE community.
![Comments](/static/assets/commentssection.png)


### Scalability and Future Development
MOONTUBE's design and architecture offer a solid foundation for scalability, allowing the platform to realize its full potential by seamlessly incorporating advanced features. The modular and well-structured codebase facilitates the integration of the following enhancements:

1. **Wallet Connect**

- Extending the user management system to accommodate wallet addresses or identifiers will enable secure wallet connections.
- User profiles and settings can be updated to include wallet-related information, facilitating cryptocurrency transactions.

2. **Payment Options**

- Integration of multiple payment options can be achieved with ease. User accounts can be enhanced to store various payment information, enabling payments for premium content, subscriptions, and donations. Integration with external payment gateways can be seamlessly implemented.

3. **P2P Chat**

- Building a peer-to-peer (P2P) chat system can leverage the existing user account and profile framework. Real-time messaging features can be added, either through web sockets or by integrating a third-party messaging service. Notifications can be effortlessly integrated with the existing notification system.

4. **Advertising Space**

- Implementing an advertising system can be done without disrupting the user experience. Ad placements and content can be managed dynamically and delivered based on user profiles and preferences. User-specific ad targeting can be seamlessly incorporated.

5. **Like/Dislike Functionality**

- Adding like and dislike functionality is an extension of the current video system. Users can interact with videos by liking or disliking them, with these interactions stored and displayed on video pages.

6. **Follow and Favorites**
- Follow and favorites features can be integrated into user profiles, allowing users to follow other users and add videos to their favorites. These features are extensions of the existing user and video systems.

7. **User Accounts**

    MOONTUBE is constantly evolving to provide the best experience for its users. In the future, the 'User Account' feature will be enhanced to offer a wide range of capabilities, empowering registered users to maximize their experience on the platform. Here's a glimpse of what a 'User Account' will be able to do:

- **Interact Within the Community:** Registered users will have the ability to actively engage with other members of the MOONTUBE community. Interaction may include liking and sharing videos, following other users, and participating in discussions and groups related to various topics.

- **Personalize Profiles:** Users can personalize their profiles, including profile pictures, theme customization, color schemes, and layout preferences. This level of customization will allow users to tailor their MOONTUBE experience to their unique tastes.

- **Access a Personalized Dashboard:** Users will have access to a personalized dashboard providing an overview of their activities, including video views, likes, comments, and engagement metrics. This dashboard will help users track their content's performance and their impact on the platform.

- **Real-Time Notifications:** Users will receive real-time notifications for activities related to their content, profile, and interactions. This feature will ensure that users stay informed about new comments, likes, and messages, enhancing their engagement with the platform.

- **Private Messaging:** Users will be able to send private messages to other users, fostering direct communication and collaboration opportunities. Messaging will enable discussions related to potential partnerships, content creation, and project collaboration.

These enhancements can be seamlessly implemented due to the platform's templated design and structured codebase. MOONTUBE's existing database schema and user management system can readily accommodate additional data fields and functionalities required for these new features. 

## Wireframe
Original Concept designed on https://lucid.app/lucidchart/715afd59-92e4-46b0-8a30-d91f3ab52811/edit?view_items=-Lors2m-M-WZ&invitationId=inv_d731e78f-3b66-4940-b1f8-5e72a4a73789

![MOONTUBE Wireframes](/static/assets/landing_wf.png)
![MOONTUBE Wireframes](/static/assets/profile_wf.png)

## Technologies Used
MOONTUBE leverages a range of technologies to ensure a seamless user experience:

- **HTML5** for structuring the content.
- **CSS** for styling and layout.
- **JavaScript** for interactive features.
- **Font Awesome** for icons.
- **Materialize CSS** for enhanced styling.
- **Google Fonts** to enhance typography.
- **JQuery** for dynamic behavior.
- **Python** for server-side scripting.
- **Flask** for web application framework.
- **MongoDB** for the database.
- **Jinja templating** for rendering dynamic content.
- **YouTube** for integrating and managing video content.
- **Git and GitHub** for version control and project hosting.

MOONTUBE combines a mix of front-end and back-end technologies to deliver a user-friendly and feature-rich platform for crypto enthusiasts, investors, developers, and content creators.


## Testing

### User Stories Testing
Here's how MOONTUBE fulfills the expectations of its users:

- **Navigating through MOONTUBE is intuitive, thanks to its user-friendly layout and easily accessible content.** The platform has been meticulously designed with user experience in mind, ensuring that users can effortlessly find their way around and access the content they seek.

- **The platform effectively serves its purpose by connecting the crypto community with influencers and opportunities.** MOONTUBE's core functionality is tested to ensure that it seamlessly connects users with influencers, crypto projects, and investment opportunities, meeting the expectations of a diverse user base.

- **MOONTUBE offers Youtube hosted video playback with user-friendly controls, enhancing the overall user experience.** Video playback and controls are tested to provide a seamless streaming experience, ensuring that users can enjoy content without interruptions. Videos hosted on YouTube are seamlessly embedded into iframes on MOONTUBE.

- **Users can create accounts, manage videos, and actively engage within the community.** All user-related features are extensively tested to guarantee that users can easily create accounts, manage their videos, and actively participate in community interactions.

- **The design and color scheme contribute to an appealing user experience.** MOONTUBE's visual elements and design choices are tested to enhance the overall appeal of the platform, contributing to an attractive and engaging user experience.

Testing MOONTUBE against these user stories ensures that the platform delivers on its promises and provides a user-friendly and engaging experience for all its users.


### Validator Testing
- **HTML**: The validator can not interpret the Jinja templating.  But other then that the code passes.
![HTML Validator](/static/assets/htmlval1.png)
![HTML Validator](/static/assets/htmlval2.png)

- **CSS**: No errors found
![CSS Validator](/static/assets/cssval.png)

- **Python**: No errors
![Python Validator](/static/assets/pythonval.png)

- **JavaScript**: No Errors


### Automated vs Manual Testing

In the testing process of MOONTUBE, I employed a combination of automated and manual testing approaches, each serving specific purposes depending on the nature of the testing required.

**Automated Testing**:
In this straightforward test, I created a function to make sure the app's main page ('/') is working correctly. It does this by sending a request to the main page and checking the response's status code. If the status code is 200, it means everything is working as expected, and we print out the test result. 

    # Test
    def test_get_videos_route():
        response = app.test_client().get('/')
        print("Test Result:", response.status_code)
        assert response.status_code == 200

**Manual Testing**:
Manual testing plays a critical role in evaluating the user experience and ensuring that MOONTUBE meets its user stories effectively. This approach is suitable for exploring the platform in a manner that closely simulates the actual user experience. Manual testing is ideal for assessing the intuitiveness of navigation, the appeal of the design, and the overall user satisfaction. It is also used to validate complex scenarios that are difficult to automate and to ensure that the platform aligns with the established user stories.

By combining automated testing for robust functional testing and manual testing for user-centric and exploratory testing, we ensure that MOONTUBE delivers a reliable and user-friendly experience.


## Manual Tests

1. **User Registration and Login**:
   - I tested the user registration process by creating a new account with a unique username and password.
   - I logged in with the newly created account to verify that the login functionality works.
   - I also tried logging in with incorrect credentials to ensure that the system handles authentication errors properly.

2. **Video Upload**:
   - After logging in as a registered user, I tried embedding a video using the YouTube URL and checked if they were processed correctly.
   - I verified that I could add video details such as title, description, and category during the upload process.

3. **Video Playback**:
   - Navigating to the main page, I clicked on various video thumbnails to play them.
   - I made sure that the video player functioned correctly, allowing me to pause, play, adjust volume, and enter full-screen mode.
   - I checked for smooth video streaming without interruptions.

4. **Search Functionality**:
   - I used the search feature to look for specific videos by keywords or phrases.
   - I confirmed that the search results were relevant to my query and that the search functionality worked as expected.

5. **User Profile**:
   - After logging in, I visited my user profile and verified that it displayed my uploaded videos.
   - I also tried editing my profile information to ensure that the changes were saved correctly.

6. **Video Comments**:
   - While playing a video, I left comments to ensure that the comment section was functional.
   - I checked if comments were displayed correctly under the video.

7. **Category Management**:
   - As an admin, I added a new category to the system and verified that it appeared in the category list.
   - I attempted to edit or delete a category and confirmed that these actions worked without errors.

8. **User Management**:
   - As an admin, I added a new user to the system, and I verified that the new user appeared in the user list.
   - I also tried editing or deleting a user account, ensuring these actions worked as intended.

9. **Security Testing**:
   - I attempted to access pages or features I shouldn't have access to (e.g., admin functions) to ensure that access controls were properly implemented.

10. **Cross-Browser Testing**:
    - I tested the website on different web browsers (e.g., Chrome, Firefox, Safari, Edge) to ensure compatibility and functionality across various platforms.

11. **Mobile Responsiveness**:
    - I accessed the website from different mobile devices (smartphones and tablets) to confirm that it was responsive and functioned well on smaller screens.

12. **Performance Testing**:
    - I observed the load times of various pages and video playback to ensure that the website performed adequately.

13. **Usability Testing**:
    - I asked a group of real users to navigate the website and provide feedback on their experience, paying attention to any usability issues, confusion, or suggestions for improvement.

These manual tests helped ensure that the website functions as expected, provides a positive user experience, and maintains security and stability.

# Data Schema

### MongoDB Collections

1. **Categories**

- `_id`: Unique identifier for the category.
- `category_name`: Name of the category.

2. **Comments**

- `_id`: Unique identifier for the comment.
- `user`: User who posted the comment.
- `text`: Text of the comment.
- `video_id`: Identifier of the video to which the comment is associated.

3. **Users**

- `_id`: Unique identifier for the user.
- `username`: Username of the user.
- `password`: Hashed password of the user.
- `email`: Email address of the user.
- `about_me`: User's profile description.

4. **Videos**

- `category_name`: Name of the category to which the video belongs.
- `video_title`: Title of the video.
- `video_description`: Description of the video.
- `video_link`: Link to the video.
- `created_by`: Username of the user who created the video.

### Collection Relationships

- Users are associated with videos they create.
- Comments are associated with videos through the `video_id`.
- Categories are associated with videos through the `category_name`.

### Database Configuration

The MongoDB database used for Moontube is named "Moontube_Database." The data is organized into the specified collections, each serving a specific purpose within the platform. The schema has been designed to efficiently store and manage information related to categories, comments, users, and videos, ensuring seamless interaction and content creation within the Moontube ecosystem.

To maintain the MongoDB database configuration in one location, a configuration file (e.g., `config.py`) includes the connection settings, such as the database name, host, and port. This centralized approach simplifies future configuration changes, ensuring that your database setup remains consistent across your application.


### Unfixed Bugs

1. **Admin Portal Redirection Issue**:
    - **Description**: When logged in as an admin and within the 'All Videos' section of the admin portal, there's an issue where, after editing another user's video or exiting the page, the admin is redirected to their own profile page instead of the admin portal.
    - **Suspected Cause**: This issue may stem from the fact that both admins and regular users use the same edit video page. After editing a video, the system defaults to returning users to their own profiles, leading to the unintended redirection for admins.
    - **Attempted Fix**: Attempts were made to implement specific if statements to address this scenario, but the desired result was not achieved. The redirection issue remains unfixed.

            if "user" in session and session["user"] == "admin":
                return redirect(url_for("admin_videos"))
            else:
                return redirect(url_for("get_categories"))

2. **Video URL Preview Discrepancy**:
    - **Description**: On the 'Add Video' page, when pasting a new video URL, a preview of the video is displayed as expected. However, on the 'Edit Video' page, the existing or previously entered URL does not generate a preview.
    - **Issue Analysis**: This issue appears to be related to the functionality disparity between the 'Add Video' and 'Edit Video' pages. The 'Add Video' page successfully generates a video preview, while the 'Edit Video' page does not provide this feature for existing URLs.
    - **Unresolved State**: Despite efforts to ensure consistency in this feature, the bug remains unfixed.

    **Edit Video**:
![Video Preview EDIT](/static/assets/editvid.png)

    **Add Video**:
![Video Preview ADD](/static/assets/addvid.png)


## Deployment

MOONTUBE is successfully deployed on Heroku, You can access the live site at [Moontube Website Link](https://moontube-db-1e90f4bf79ae.herokuapp.com/).

## Credits

### Moontube vs Task Manager

Moontube has leveraged the technology and architecture of the Code Institute Flask Task Manager project, introducing significant modifications to create a streaming platform. The project's foundation builds upon the Flask Task Manager's architecture, emphasising the adaptability and reusability of technology across diverse use cases.

**User Profiles and Streaming**

Moontube's core functionality revolves around user profiles. Utilizing a system derived from the Flask Task Manager, these profiles are tailored to facilitate content creation, video streaming, and community interaction. This transformation showcases Moontube's entirely different needs providing an engaging crypto streaming platform for users.

**Database Management and MongoDB**

Similar to the Flask Task Manager, Moontube maintains the CRUD (Create, Read, Update, Delete) database practices at its core. While the Task Manager managed tasks, Moontube utilizes these practices to handle video content, comments, and user interactions. MongoDB continues to play a vital role in Moontube. 

**Deployment on Heroku**

In line with the Flask Task Manager's deployment approach, Moontube is hosted on Heroku, ensuring scalability and accessibility for a broad user base. Heroku's reliability for web applications supports Moontube in reaching a wide audience.


### Content
Javascript to embed Youtube URL was taken from these videos.
- https://www.youtube.com/watch?v=3OlTKaGVMIA
- https://www.youtube.com/watch?v=aPUVUrS2oC0

Inspiration for layout from this tutorial
- https://www.youtube.com/watch?v=4ykAepVkG5Y&t=2s

- Flask and Jinja Templating ideas from here
https://www.youtube.com/watch?v=4yaG-jFfePc

- Redirects, Returns and User restriction 
https://stackoverflow.com/questions/67610712/how-do-i-restrict-an-users-access-with-flask-principal-and-flask-security

### Media
- All Videos are from Youtube and the content is owned by the creators.  For Demo purposes, videos not created by the Moontube profile name/ User have been used.  This was to simulate a functional site with working content
- The Logo was designed by Anthony Hayes
- The Background Image is from Adobe Express



