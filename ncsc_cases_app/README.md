# Instructions for Installation and Execution

# Installation
1. Ensure you have the `Python` programming language installed - if you have python 3 installed you will be using the `python3` command, if you do not, then you will use the `python` command
2. Ensure you have the `pip` package manager installed by following the instructions on this page `https://pip.pypa.io/en/stable/installation/`
3. Using the terminal navigate to the folder of the code submission with the files `manage.py` and `requirements.txt`. This will be in `ssd_ncsc_app/ncsc_cases_app/`
4. Use the command `pip install -r requirements` to install all project dependencies. These dependencies are necessary for the project to run and include things like django-crytography for database encryption or django framework itself. Please see the requirements.txt file for the full details.
5. Once all dependencies are installed, use the command `python manage.py runserver` or `python3 manage.py runserver` to run the server application and all services.
6. Next, navigate to a web browser and enter the URL localhost:8000 to run the application

The home page of the app will now be displayed on the screen.
![image](https://github.com/haarismian/ssd_ncsc_app/assets/13083798/3b424159-bd35-435d-a5f8-4d4fa87413a5)

# Functional Requirements
All functional requirements were implemented in the system as designed. Please see a list below:

### Non-Authenticated Users
Users who have not logged in are only able to perform two actions: view active cases and submit a CVD Report.

#### 1. View Active Cases
To view a current list of active cases, click the `View All Cases` button on the home screen. Under actions, click the `View Case` button to see the details of any given case (Author, Case ID, Title, and Case Description).
![image](https://github.com/haarismian/ssd_ncsc_app/assets/13083798/1dd6297a-8f90-4def-8ed2-cbfd3f41c28c)

#### 2. Submit CVD Report
To submit a CVD report, click on the `Submit CVD Report` button on the home page. Fill out the form with your personal details and the details of the vulnerability. Click the `Create` button.
![image](https://github.com/haarismian/ssd_ncsc_app/assets/13083798/69456b0b-b610-42e6-ad9c-2c3536f6f8a7)

### Authenticated Officer Users
Registered users are able to perform more actions than non-users.

Default Username  | Default Password
------------------| ----------------
ssd_team2         | ssd_password

#### 1. Login
Click the login link on the home page or the login tab on the navigation bar. Enter the username and password (provided above). This will then direct you to a personalized home page.

#### 2. View Active Cases
On the home page, click the `View List of Currently Active Cases` button. The Case List Page will display a list of currently active cases with the title and ID. To view a case in more detail, click the `View Case` button.

#### 3. Delete Cases
From the Case List page, click the blue `Create New Case` button at the top of the page. Fill out the form with your personal details as well as the vulnerability details. Click the `Submit` button.

![image](https://github.com/haarismian/ssd_ncsc_app/assets/13083798/ae21f827-a8b0-4f34-aebf-d05c3d1209d8)

#### 4. View all CVDs, delete CVDs, and View Single CVD in Detail
To view the CVD Report List, click the `Go to CVD page` button on the home page. This will allow you to view the details of all CVD Reports that have been submitted, as well as an option to view, delete, or create CVDs.

![image](https://github.com/haarismian/ssd_ncsc_app/assets/13083798/2f62c329-da83-47e5-8c96-95f5e50445c9)


### Create New Users

Default Admin Login | Default Admin Password
--------------------| -----------------------
ncsc_admin          | ssd_password


Our application also allows for the creation of new users, which can only be done by administrator accounts. Go to the admin portal at **http://localhost:8000/admin**. Enter the administrator username and password. Once logged in, new users can be added by selecting the new user's username and password. Once created, enter the new user's personal information (such as name and email) as well as permissions (such as active, staff, and super user status) and groups. Once the form is filled out completely, click the `Save` button at the bottom of the screen.

# Security Features (See supplemental document for evidence of testing):
1. Automatic session timeout - 5 minutes of inactivity.
2. Role-based authentication 
3. Logging and Monitoring - All API calls, DB queries, and warnings such as failed login attempt
4. Automated logging response - for example block IP after multiple failed login attempts
5. XSS, CSRF, and SQL injection projection
6. PEP8 Style guide linter
7. Hashed and encrypted passwords and personally identifying information
8. Cookie consent
9. Form validations


# Changes from the Design Document
* Frontend is no longer in React. Instead, the application is fullstack in Django and uses Django template language as the frontend.
* Instead of using PostgreSQL, the application now uses SQLite, which is supported by Django. Encryption is provided by Django-cryptography library
* The application is now used locally instead of remotely.
