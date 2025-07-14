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

*Prepared by: [Krishna Sharma]*  
*Date: July 14, 2025*