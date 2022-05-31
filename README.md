Repository name: Frewards
Test Backend Assessment for Fetch Rewards

Motivation

This project was completed as part of an assessment for the Fetch Rewards Apprenticeship.

Build Status
This is not a complete backend, but a sample based on the requirements received from Fetch. For this particular app, it was assumed that the developer is accessing one particular user’s account in order to check their reward points. All the information was hard-coded, although in the real world it would have been added to a relational database and accessed from there instead of storing it in memory.

Code Style
The code was written in the standard style. There are comments throughout the code so as to guide the person looking at the files as to what the code snippet was intended for (when it isn’t obvious). The names chosen for the functions and variables are descriptive and easy to understand and follow

Frameworks
This project was completed using Django 4.0.2

Instructions to install Django:
Open a Terminal window (you can do this through an editor, like VSCode or directly through your Terminal
You can install Django globally on your machine simply by entering the command pip install django This will install the latest version of Django.
Wait for the installation to be completed, and check that it was installed correctly by entering the command django-admin —version in your terminal’s command prompt.
Another option is to install Django in a virtual environment, instructions for that can be found here

Instructions to run the Django server:
Once Django has been installed, the project can run in the server in the following way:
Through your terminal window access the directory where you saved the folder containing this project
look for the directory that contains the manage.py file
in your terminal command window enter: python manage.py runserver (for windows), or python3 manage.py runserver (for macOs).
Once the server is up and running, enter localhost:8000 in the web browser window. That should lead to the homepage of the project.

API reference
This is a very simple API and all of its functions can be accessed by using the links provided on the navigation bar.
Each page is related to a specific function (all the functions used in this project can be found in the views.py file, and the URLs are located in the urls.py files).
Django uses functions (views) and display the results of said functions in an HTML page using templates. These templates use Django Template Language to allow access to variables from a defined context. More information on this topic can be found here

How to use this app
To use the app, it is only necessary to run the server and follow the links provided in the navigation bar in order to find the desired information.
For a more interactive approach, it is possible to change the values of the initial list of dictionaries by going to the views.py file and changing the data manually (again, this is not the optimal way to do it, but simply an example).
It is also possible to change the values of local variables inside the functions found in views.py. Since this project was created as a sample, this information is saved in memory instead of a database (no models —Django’s name for tables— were created for this project, although in a real-life application this would be the appropriate way of building the backend). Also, the values provided for variables are hard coded instead of using a more dynamic approach like Django Forms.
