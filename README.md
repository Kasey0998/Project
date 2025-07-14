# Apartment Management System  
## Project Report

---

## 1. Introduction

The GomataVision CRM System is a web-based platform designed to streamline the management of apartments, users, client leads, and sales activities. Built using Flask, SQLAlchemy, and Flask-Login, the system provides role-based access for administrators, marketing, and sales teams, ensuring efficient workflow and secure data handling.

---

## 2. Key Features

- **Role-Based Access:** Supports Admin, Marketing, and Sales roles with tailored dashboards and permissions.
- **User Authentication:** Secure login/logout functionality with Flask-Login.
- **Admin Capabilities:** Manage users, apartments, and view real-time dashboard statistics.
- **Marketing Workflow:** Add and track client leads, view pending leads.
- **Sales Workflow:** Update lead status (sold/not interested), manage sales pipeline.
- **Dashboard:** Real-time statistics and analytics for administrators.

---

## 3. System Architecture

### 3.1 Folder Structure

```
app.py
requirements.txt
models/
    __init__.py
    apartment.py
    user.py
routes/
    admin.py
    auth.py
    dashboard.py
    marketing.py
    sales.py
static/
    css/
        style.css
templates/
    base.html
    login.html
    admin.html
    admin_users.html
    admin_apartments.html
    edit_user.html
    edit_apartment.html
    dashboard.html
    marketing.html
    sales.html
    unauthorized.html
instance/
    apartment.db
```

### 3.2 Main Components

- **Models:**  
  - `User`: Handles authentication and user roles.  
  - `Apartment`: Represents apartment buildings.  
  - `Flat`: Represents individual flats.  
  - `ClientLead`: Tracks client leads and their status.

- **Routes:**  
  - `auth.py`: Authentication (login/logout).  
  - `dashboard.py`: Dashboard views for each role.  
  - `admin.py`: Admin management for users and apartments.  
  - `marketing.py`: Lead management for marketing.  
  - `sales.py`: Sales processing and lead updates.

- **Templates:**  
  - HTML templates for each page and role-specific dashboard.

- **Static:**  
  - CSS for styling.

---

## 4. Setup Instructions

1. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```
   python app.py
   ```

3. **Default Admin Credentials**
   - Username: `admin`
   - Password: `admin123`

---

## 5. Database

- Uses SQLite (`instance/apartment.db`) by default.
- Tables are auto-created on first run.
- Can be configured for other databases via SQLAlchemy.

---

## 6. Customization & Security

- Update `app.secret_key` in `app.py` for production use.
- Change the database URI in `app.py` as needed.

---

## 7. Conclusion

This Apartment Management System provides a robust, scalable, and secure solution for managing apartment-related operations. Its modular design and role-based access make it adaptable for various organizational needs.

---

## 8. References :
Flask code : https://flask.palletsprojects.com/en/stable/quickstart/
Flask code : https://palletsprojects.com/
Flask code : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
Flask code : https://www.geeksforgeeks.org/python/flask-tutorial/
Folder structure : https://explore-flask.readthedocs.io/en/latest/organizing.html  
Blueprints : https://explore-flask.readthedocs.io/en/latest/blueprints.html
Blueprints : https://flask.palletsprojects.com/en/stable/tutorial/views/
Flask login : https://flask-login.readthedocs.io/en/latest/
Routing : https://realpython.com/primer-on-jinja-templating/
Routing : https://www.geeksforgeeks.org/python/flask-app-routing/
Flask login : https://flask-login.readthedocs.io/en/latest/
MySQL Alchemy : https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
MySQL Alchemy : https://docs.sqlalchemy.org/en/20/orm/



## Harvard style referencing :

- Flask, (n.d.). *Quickstart — Flask Documentation*. [online] Available at: https://flask.palletsprojects.com/en/stable/quickstart/ 

- Pallets Projects, (n.d.). *Pallets Projects*. [online] Available at: https://palletsprojects.com/ 
  
- Grinberg, M., (2017). *The Flask Mega-Tutorial Part I: Hello, World!*. [online] Available at: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
  
- GeeksforGeeks, (n.d.). *Flask Tutorial*. [online] Available at: https://www.geeksforgeeks.org/python/flask-tutorial/

- Explore Flask, (n.d.). *Organizing your project*. [online] Available at: https://explore-flask.readthedocs.io/en/latest/organizing.html  

- Explore Flask, (n.d.). *Blueprints*. [online] Available at: https://explore-flask.readthedocs.io/en/latest/blueprints.html 

- Flask, (n.d.). *Views and Blueprints — Flask Tutorial*. [online] Available at: https://flask.palletsprojects.com/en/stable/tutorial/views/ 

- Flask-Login, (n.d.). *Flask-Login Documentation*. [online] Available at: https://flask-login.readthedocs.io/en/latest/   

- Sturtz, C., (2021). *A Primer on Jinja Templating*. [online] Real Python. Available at: https://realpython.com/primer-on-jinja-templating/   

- GeeksforGeeks, (n.d.). *Flask App Routing*. [online] Available at: https://www.geeksforgeeks.org/python/flask-app-routing/ 

- TutorialsPoint, (n.d.). *Flask - SQLAlchemy*. [online] Available at: https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm   

- SQLAlchemy, (n.d.). *SQLAlchemy ORM Documentation*. [online] Available at: https://docs.sqlalchemy.org/en/20/orm/ 


*Prepared by: Krishna Sharma*  
*Date: July 14, 2025*