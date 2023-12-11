# django-x-clone

This project was created to apply my Django knowledge by attempting to replicate X

![django-x-clone-home-page](https://github.com/anthohn/django-x-clone/assets/75019251/9e65d060-f107-4b6d-b9f1-2519386c7bf4)


## Overview

The main goal of this project is to develop a web application **only** by using the Django framework to create a website where users can create posts, follow other users, and interact with content similar to the X application.

## Planned Features

- **User Authentication:** Allow users to register, log in, and manage their profiles.
- **Post Creation:** Enable users to create short messages, similar to tweets.
- **User Following:** Allow users to follow other users to see their posts in their feed.
- **Interactions:** Implement features such as likes, retweets, and comments on posts.
- **Search:** Add a search feature to allow users to find other users or specific posts.

## Development Environment

1. Clone the project:
````
git clone https://github.com/anthohn/django-x-clone.git
````
2. Navigate to the project directory:
````
cd django-x-clone
````
3. Create virtual  environment :
````
py -m venv ENV
````
4. Activate the virtual envrionment :
````
env\Scripts\activate
````
5. Install dependencies :
````
pip install -r requirements.txt
````
6. Install TawilwindCss :
````
py manage.py tailwind install
````
7. Apply migrations :
````
py manage.py migrate
````
8. Run the development server :
````
py manage.py runserver
````

**Note:** This project is developed for educational purposes and to practice Django skills. It is not affiliated with X.
