<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer">
 <img src="![logo1](https://github.com/ahmbana90/TopiTalk/assets/124783249/397a43e2-79e0-44e2-93a5-a6ae9e461fa3)" alt="python" width="40" height="40"/> </a> </p>


# TopiTalk 

## Overview

My project is a **Django** web application designed to create discussion rooms to talk about different topics and have open discussion.
The user can navigate through the different rooms  or topics that was created or check out the the rooms that are related to a certain topic, or can create a new room with a new topic.

## Technologies Used

<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer">
 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> </a> </p>



## Project Structure

Here's an overview of the project directory structure:

``` 
TopiTalk/
├── base
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_user_bio_user_name_alter_user_email.py
│   │   ├── 0003_user_avatar.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_alter_room_options_room_participant.cpython-310.pyc
│   │       ├── 0002_message.cpython-310.pyc
│   │       ├── 0002_user_bio_user_name_alter_user_email.cpython-310.pyc
│   │       ├── 0003_rename_participant_room_participants.cpython-310.pyc
│   │       ├── 0003_user_avatar.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── tests.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── templates
│   │   └── base
│   │       ├── activity_component.html
│   │       ├── activity.html
│   │       ├── delete.html
│   │       ├── feed_component.html
│   │       ├── home.html
│   │       ├── login_register.html
│   │       ├── profile.html
│   │       ├── room_form.html
│   │       ├── room.html
│   │       ├── topics_component.html
│   │       ├── topics.html
│   │       └── update-user.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── confi
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Makefile
├── manage.py
├── README.md
├── requirements.txt
├── static
│   ├── images
│   │   ├── avatar.svg
│   │   ├── browser-logo.png
│   │   ├── favicon.ico
│   │   ├── icons
│   │   │   ├── add.svg
│   │   │   ├── arrow-left.svg
│   │   │   ├── chevron-down.svg
│   │   │   ├── delete.svg
│   │   │   ├── edit.svg
│   │   │   ├── ellipsis-horizontal.svg
│   │   │   ├── ellipsis-vertical.svg
│   │   │   ├── lock.svg
│   │   │   ├── remove.svg
│   │   │   ├── search.svg
│   │   │   ├── sign-out.svg
│   │   │   ├── tools.svg
│   │   │   ├── user-group.svg
│   │   │   └── user.svg
│   │   ├── logo1.svg
│   │   ├── meeting.png
│   │   ├── wallpaper_0lsHBQA.jpg
│   │   ├── wallpaper1.jpg
│   │   ├── wallpaper.jpg
│   │   └── web.png
│   ├── js
│   │   └── script.js
│   └── styles
│       └── style.css
└── templates
    ├── main.html
    └── navbar.html
   
``````


## Features

Key features of my project include:

1. User Authentication
   - Users can create accounts and log in.

2. Profile page
   - Users can view their profile and display a bio about themselves.
   - Users can view rooms that was created by them.

3. Data Visualization
   - On the home page users can go through all rooms created by other users.
   - Users can see the latest top feeds in a clickable manner with the room name and the username who created each feed.

## Screenshots

Here are some screenshots from the project:
 ![Screenshot from 2023-10-07 04-30-00](https://github.com/ahmbana90/TopiTalk/assets/124783249/f2eb1311-e83d-42fd-bc16-97fd48484dd7)
 
 ![Screenshot from 2023-10-07 04-30-11](https://github.com/ahmbana90/TopiTalk/assets/124783249/2f1d6a36-f3d6-4354-88ed-c962076f7b87)
 
 ![Screenshot from 2023-10-07 04-30-52](https://github.com/ahmbana90/TopiTalk/assets/124783249/a2745846-5da0-4bd1-85d0-eab8edd1b43c)

Mobile version:

 ![Screenshot from 2023-10-07 04-28-42](https://github.com/ahmbana90/TopiTalk/assets/124783249/9d56ec2d-d3be-420a-a87e-fb73ca5513fc)

## Installation

To set up my project, follow these steps:

1. Clone the repository(SSH):

   ```bash
   git clone git@github.com:ahmbana90/TopiTalk.git
   ``````
2. Move into the directory where the project files are saved:

   ```bash
   cd TopiTalk
   ``````
3. Create a virtual environment:

   ```bash
   Python3 -m venv .venv
   ``````
4. Create a Postgres database:

   ```bash
   CREATE DATABASE topi_talk;
   ``````
5. Activate virtual environment:

   ```bash
   source .venv/bin/activate
   ``````
6. Install requirements:

   ```bash
   pip install -r requirements.txt
   ``````
7. Perform database migrations:

   ```bash
   python manage.py migrate
   ``````
8. Run the development server:

   ```bash
   python manage.py runserver
   ``````

