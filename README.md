# Lumo Property Marketplace 

## Overview
Lumo is a marketplace application for listing, searching, and managing properties for sale or rent. The platform allows user to:
* Sign up and create an account.
* List properties for sale or rent.
* Search for properties based on various criteria.
* View detailed information about a property.
* Update or unlist properties as needed.
This document provides an overview of the application's features, architecture, and usage guidelines.


## Features
### 1. User Authentication
* Sign Up: Users can create an account by providing a username, email, phone number, whatsApp number (optional) and password.
* Login: Users log in using their registered credentials.
* Session Management. Logged-in sessions persist securely using cookies or tokens.

### 2. Property Listings
* Create Listing: Users can add property details such as title, description, price, location, and images.
* Manage  Listings:
    * Update property details.
    * Unlist properties when no longer available.
* View Listings: Detailed pages show all property information and associated images.

### 3. Property Search
* Search Bar: Users can search properties by keywords, description, or title.

### 4. User-Friendly Interface
* Designed using Bootstrap for responsiveness and ease of use.
* Consistent design and easy navigation.

## Technology Stack
### Backend
![Flask](static/images/flask_logo.png) ![MySQL](static/images/mysql_logo.png)
* Authentication: Flask-Login (app) and Flask JWT Extension (api)
* ORM: SQLAlchemy

### Frontend
![Jinja2](static/images/jinja_logo.png) ![Bootstrap](static/images/bootstrap_logo.png) ![JS](static/images/js_logo.png)

### Deployment
* Server: Hosted on Python Anywhere
* Static Files: Served through Flask's static folder.


## Database Schema

### User Table
|Field       | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| id         | VARCHAR(255)  | Unique user id                |
| username   | VARCHAR(64)   | Username of the user          |
| email      | VARCHAR(255)  | User email address            |
| password_hash | VARCHAR(255) | Hashed_password |
| created_at | DATETIME | Account creation timestamp |
| updated_at | DATETIME | Account update timestamp |

### Properties Table
|Field       | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| id | VARCHAR(64) | Unique property ID |
| title | VARCHAR(255) | Title of the property |
| description | TEXT | Detailed property description |
| price | FLOAT | Price of the property |
| location | VARCHAR(255) | Property location |
| user_id | VARCHAR(64) | ID of the property owner |
| created_at | DATETIME | Listing creation timestamp |
| updated_at | DATETIME | ID of the property owner |


### Images
|Field       | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| image_url | VARCHAR(255) | URL of image |
| property_id | VARCHAR(64) | ID of the property |
| created_at | DATETIME | Image added timestamp |

### Amenities
|Field       | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| name | VARCHAR(32) | Name of the amenity |
| amount | INT | Quantity of the amenity |
| created_at | DATETIME | Amenity added timestamp |

### Regions
|Field       | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| name | VARCHAR(60) | Name of the region |
| created_at | DATETIME | Region added timestamp |


### Areas
|Field       | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| name | VARCHAR(60) | Name of the area |
| created_at | DATETIME | Area added timestamp |


### Cities
|Field       | Type          | Description                   |
| ---------- | ------------- | ----------------------------- |
| name | VARCHAR(60) | Name of the city |
| created_at | DATETIME | City added timestamp |


## API Endpoints

### Authentication & User Management
* POST /auth/signup: Register a new user.
* POST /auth/login: Log in an existing user.
* GET /auth/logout: Log out the user.
* GET /users/me: Get the currently authenticated user's details.
* PATCH /users/me: Update the currently authenticated user's profile
* DELETE /users/me: Deactivate/delete the currently authenticated user's account


### Property Management
* GET /properties: Retrieve a list of all properties.
* GET /properties/search: Search for a property.
* POST /properties: Create a new property listing.
* PATCH /properties/{id}: Update an existing property listing.
* DELETE /properties/{id}: Unlist a property

### images
* DELETE /images/{id}: Delete a specified image

### Admin Management
* GET /admin/users: Get a list of all users (only)
* PATCH /admin/users/{user_id}: Update specific a specific user by admin
* DELETE /admin/users/{user_id}: Deactivate/delete specific user by admin.
* POST /admin/regions: Add a new region (admin only).
* PATCH /admin/regions/{region_id}: Update a specific region (admin only). 
* DELETE /admin/regions/{region_id}: Delete a specific region (admin only).
* POST /admin/regions/{region_id}/areas: Add a new area under a region (admin only).

* PUT /admin/areas/{area_id}: Update a specific area (admin only).
* DELETE /admin/areas/{area_id}: Delete a specific area (admin only).
* POST /admin/areas/{area_id}/cities: Add a new city under an area (admin only).
* PATCH /admin/cities/{city_id}: Update a specific city (admin only).
* DELETE /admin/cities/{city_id}: Delete a specific city
* POST /admin/amenities: Add a new amenity
* PATCH /admin/amenities/{amenity_id}: Update a specific amenity
* DELETE /admin/amenities/{amenity_id}: Delete a specific amenity


### User Listings
* GET /users/{user_id}/properties: Get all properties listed by a specific user.


### Region, Area, City and Amenity
* GET /regions: Get a list of all regions.
* GET /regions/{region_id}: Get details of a specific region.
* GET /areas/{area_id}/: Get details of a specific area.
* GET /regions/{region_id}/areas: Get details of a specific area.


## Usage
### Setting Up the Application
#### 1. Clone the Repository:
```bash
$ git clone https://github.com/AtcoCoder/lumo.git
$ cd lumo
```
#### 2. Set Up the Environment:
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirement.txt
```

#### 3. configure the Database:
* Update the config/ init file. Replace the MySQL credentials in curl brackets with yours.

`$ vim config/__init__.py`
```vim
# config/__init__.py
# the configuration file

.
.
.
CURRENT_CONFIG.DATABASE_URI = 'mysql+mysqlconnector://{your_mysql_username}:{password}@localhost/{database_name}'
```

#### 4. Run the Application
* Run the flask web app:
`$ CONFIG=DEVELOPMENT python3 -m web_flask.run`

* Run the api:
`$ CONFIG=DEVELOPMENT python3 -m api.v1.app`

### Accessing the Application
* Open your browser and navigat to `http://localhost:500`.

## Authors
* Omar Jammeh

## Contact
For contribution or inquiries, email at orms45@gmail.com.