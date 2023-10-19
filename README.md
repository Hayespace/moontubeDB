# MOONTUBE - All-in-One Crypto Community Platform

![responsiveness](/static/assets/responsiveness.png)

**Visit MOONTUBE at [Moontube](https://moontube-db-1e90f4bf79ae.herokuapp.com/)**

Welcome to MOONTUBE, the platform for connecting investors, crypto developers, and YouTubers all in one place. MOONTUBE streamlines the crypto community by providing a secure space to find influencers, create marketing opportunities, and promote projects. MOONTUBE simplifies the crypto experience with just a click.

## Table of Contents
1. [User Stories](#user-stories)
2. [Design and Color Scheme](#design-and-color-scheme)
3. [Features](#features)
4. [Wireframe](#wireframe)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Data Schema](#data-schema)
8. [Unfixed Bugs](#unfixed-bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)

## User Stories

In the world of cryptocurrency, the term "moon" is a popular slang term used by enthusiasts and traders. It refers to a significant and often rapid increase in the price of a cryptocurrency, resulting in substantial profits for those who hold the asset. When a cryptocurrency is said to be "mooning," it means that its value is soaring to new heights, reaching a point where the investors who believed in it early on are reaping substantial financial rewards. The use of "moon" in cryptocurrency is closely tied to the idea of reaching the moon, a metaphor for achieving great financial success through investments.

The relevance of the name MOONTUBE for a streaming platform in the crypto space is multi-fold:

- **Positive Connotation:** The term "moon" in the context of cryptocurrency is associated with optimism and profit. It represents the ultimate goal for many crypto investors - seeing their investments skyrocket in value. By incorporating "moon" into the name, MOONTUBE aligns itself with this positive and ambitious sentiment.

- **Community Engagement:** Cryptocurrency communities often use the concept of "moon" to create excitement and engagement. MOONTUBE, as a streaming platform, can tap into this enthusiasm by providing a space for enthusiasts to share their experiences, insights, and knowledge, further fueling the ambition to reach the moon.

- **Crypto Lifestyle:** MOONTUBE's name suggests that it's not just about the financial aspects of cryptocurrency but also about the lifestyle and culture that surrounds it. Many crypto enthusiasts are passionate about the technology and its potential to change the world, and MOONTUBE can serve as a hub for discussions, collaborations, and content creation in this regard.

In summary, "moon" in the context of cryptocurrency symbolizes the dream of financial success and prosperity. MOONTUBE's name captures this spirit and invites users to be part of a community and platform that embraces the excitement and ambition of the crypto space.

MOONTUBE users will:

- **Easily Connect with Influencers:** MOONTUBE simplifies the process of connecting with influencers and exploring marketing opportunities for token developers, aligning with the optimistic and profit-driven sentiment associated with "moon" in crypto.

- **Build a Strong Community:** MOONTUBE serves as a hub for like-minded individuals, fostering connections and discussions within a single platform. It's not just about financial gains but also about the crypto lifestyle, technology, and culture that surrounds it.

- **For YouTubers, Developers, and Investors:** Whether you're a YouTuber seeking collaboration, a developer looking for secure promotion opportunities, or an investor aiming to ride the wave of a "moon" project, MOONTUBE invites you to dream big and explore the limitless potential of the crypto world.


## Design and Color Scheme

The MOONTUBE visual aesthetic is a reflection of the universe of cryptocurrencies. I have drawn inspiration from the moon and space, infusing the platform with a celestial vibe.

### Space-Inspired
Cryptocurrency, like the vastness of space, is full of possibilities. I have harnessed this inspiration to create a design that evokes the mystery and excitement of the crypto world. From the logo to the spacey hues that enhance the overall experience, you'll feel like you're embarking on a cosmic journey each time you log in.

### Sleek and Dark
The scheme is designed to be sleek, like the black canvas of outer space. The dark background provides a comfortable and immersive viewing experience, reducing eye strain during extended visits to the platform.

### Solar Flares and Lens Flares
Incorporating elements inspired by solar flares and lens flares adds dynamic energy to the design. These splashes of vivid colors represent the vibrant and ever-changing nature of the crypto market.

### 2001: A Space Odyssey Aesthetics
As a homage to the iconic film "2001: A Space Odyssey," I have included design elements that pay tribute to its visual style. The futuristic and minimalist look of the film has inspired the theme, adding a touch of sophistication to MOONTUBE.

The design and color scheme aim to make your journey through the crypto universe not only informative but also visually captivating. MOONTUBE is more than just a platform; it's an experience that immerses you in the cosmic realm of cryptocurrency.


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
  - MOONTUBE simplifies the video upload process, allowing users to customize video details such as titles and descriptions.
  - Users can also update, edit, and delete their own videos and profiles, giving them full control over their content and online presence.

### Admin Features
  - Administrators on MOONTUBE possess extensive capabilities beyond those of regular users.
  - Admins have access to all the features available to regular users and can perform additional actions, including creating, updating, and deleting other users' videos and profiles.
  - This ensures the platform's quality and adherence to guidelines.
  - Admins can also create new categories and curate the trending section, promoting content that deserves recognition within the MOONTUBE community.

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

7. **User Accouns**

    MOONTUBE is constantly evolving to provide the best experience for its users. In the future, the 'User Account' feature will be enhanced to offer a wide range of capabilities, empowering registered users to maximize their experience on the platform. Here's a glimpse of what a 'User Account' will be able to do:

- **Create Detailed Profiles:** Users will have the ability to create comprehensive profiles that showcase their personality and interests. These profiles can include personal information, profile pictures, and bios, making it easy for others to get to know them better.

- **Seamlessly Add YouTube Video Links with Descriptions:** Users will be able to integrate their YouTube video content into MOONTUBE effortlessly by adding video links along with descriptions. This feature will enable users to share their videos with the MOONTUBE community, providing a platform for exposure and engagement.

- **'For Hire' Toggle:** MOONTUBE will offer a 'For Hire' toggle switch, allowing users to indicate their availability for services. This feature will be particularly valuable for freelancers, content creators, and professionals looking to offer their skills or collaborate with others on the platform.

- **Engage Through Comments:** Users will be able to actively engage with the MOONTUBE community by leaving comments on videos posted by other users. This will encourage discussions, feedback, and interactions, creating a vibrant and supportive environment.

- **Interact Within the Community:** Registered users will have the ability to actively engage with other members of the MOONTUBE community. Interaction may include liking and sharing videos, following other users, and participating in discussions and groups related to various topics.

- **Personalize Profiles:** Users can personalize their profiles, including theme customization, color schemes, and layout preferences. This level of customization will allow users to tailor their MOONTUBE experience to their unique tastes.

- **Access a Personalized Dashboard:** Users will have access to a personalized dashboard providing an overview of their activities, including video views, likes, comments, and engagement metrics. This dashboard will help users track their content's performance and their impact on the platform.

- **Real-Time Notifications:** Users will receive real-time notifications for activities related to their content, profile, and interactions. This feature will ensure that users stay informed about new comments, likes, and messages, enhancing their engagement with the platform.

- **Robust Privacy Settings:** MOONTUBE will offer robust privacy settings, allowing users to control who can view their content, follow them, or send them messages. This will empower users to manage their online presence and protect their privacy effectively.

- **Private Messaging:** Users will be able to send private messages to other users, fostering direct communication and collaboration opportunities. Messaging will enable discussions related to potential partnerships, content creation, and project collaboration.

- **Community Support Network:** MOONTUBE will provide access to a community support network, where users can seek help, share ideas, and collaborate on projects. This feature will promote a sense of belonging and encourage users to actively participate in the MOONTUBE ecosystem.

In summary, a 'User Account' on MOONTUBE will open up a world of opportunities for users to connect, engage, and share their content with the crypto community. Whether they are content creators, investors, or crypto enthusiasts, registered users will be able to make the most of their MOONTUBE experience by leveraging these features.

These enhancements can be seamlessly implemented due to the platform's templated design and structured codebase. MOONTUBE's existing database schema and user management system can readily accommodate additional data fields and functionalities required for these new features. 

## Wireframe
![MOONTUBE Wireframes](link-to-your-wireframe-image)

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
MOONTUBE is deployed on [Your Hosting Platform]. Access the live site at [Moontube Website Link](https://moontube-db-1e90f4bf79ae.herokuapp.com/).

## Credits

### Content
- [Source of Content 1]: Description of content and attribution.
- [Source of Content 2]: Description of content and attribution.

### Media
- [Source of Media 1]: Description of media and attribution.
- [Source of Media 2]: Description of media and attribution.



