# Instructions for Installation and Execution

# Installation
To begin the installation process, open the code submission.

Enter the `python3 manage.py runserver` command to import the Django code module. Next, navigate to a web browser and enter the URL localhost:8000 to run the contents of the directory.

The home page of the app will now be displayed on the screen.



# Functional Requirements
All functional requirements were implemented in the system as designed. Please see a list below:

### Non-authenticated esers
Users who have not logged in are only able to perform two actions: view active cases and submit a CVD Report.
#### 1. View Active Cases
To view a current list of active cases, click the `View All Cases` button on the home screen. Under actions, click the `View Case` button to see the details of any given case (Author, Case ID, Title, and Case Description).


#### 2. Submit CVD Report
To submit a CVD report, click on the `Submit CVD Report` button on the home page. Fill out the form with your personal details and the details of the vulnerability. Click the `Create` button.

### Users
Registered users are able to perform more actions than non-users.

Default Username  | Default Password
------------- | -------------
ssd_team2  | ssd_password

#### 1. Login
Click the login link on the home page or the login tab on the navigation bar. Enter the username and password (provided above). This will then direct you to a personalized home page.
#### 2. View Active Cases
On the home page, click the `View List of Currently Active Cases` button. The Case List Page will display a list of currently active cases with the title and ID. To view a case in more detail, click the `View Case` button.
#### 3. Delete Cases
From the Case List page, click the blue `Create New Case` button at the top of the page. Fill out the form with your personal details as well as the vulnerability details. Click the `Submit` button.
#### 4. View all CVDs
To view the CVD Report List, click the `Go to CVD page` button on the home page. This will allow you to view the details of all CVD Reports that have been submitted, as well as an option to view, delete, or create CVDs.

### Create New Users

Default Admin Login | Default Admin Password
------------- | -------------
ncsc_admin  | ssd_password


Our application also allows for the creation of new users, which can only be done by administrator accounts. Go to the admin portal at **http://localhost:8000/admin**. Enter the administrator username and password. Once logged in, new users can be added by selecting the new user's username and password. Once created, enter the new user's personal information (such as name and email) as well as permissions (such as active, staff, and super user status) and groups. Once the form is filled out completely, click the `Save` button at the bottom of the screen.

# Security Feautres:
1. Automatic session timeout - 5 minutes of inactivity.
2. Role-based authentication

# Changes from the design document
* Frontend is no longer in React. Instead, the application is fullstack in Django and uses Django template language as the frontend.
* Instead of using PostgreSQL, the application now uses SQLite, which is supported by Django. Encryption is provided by django-cryptography library
* The application is now used locally instead of remotely.