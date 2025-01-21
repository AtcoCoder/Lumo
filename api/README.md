# API Endpoints

## Authentication & User Management

### POST /auth/signup: Register a new user.
#### Parameters
***username*** `string`
[required] The name that will appear as the owner of a listing.

***email*** `string`
[required] Email address of the user.

***phone number*** `string`
[required] Phone number of the user.

***whatsapp*** `string`
[optional] WhatsApp number of the user.

***password*** `string`
[required] User's password

#### Example request body
```json
{
    "username": "john",
    "email": "john@email.com",
    "phone_number": "12345678",
    "whatsapp": "12345678",
    "password": "password"
}
```


#### Example response
```json
{
    "message": "User successfully created."
}
```

____



* POST /auth/login: Log in an existing user.
* GET /auth/logout: Log out the user.
* GET /users/me: Get the currently authenticated user's details.
* PATCH /users/me: Update the currently authenticated user's profile
* DELETE /users/me: Deactivate/delete the currently authenticated user's account


## Property Management
* GET /properties: Retrieve a list of all properties.
* GET /properties/search: Search for a property.
* POST /properties: Create a new property listing.
* PATCH /properties/{id}: Update an existing property listing.
* DELETE /properties/{id}: Unlist a property

## images
* DELETE /images/{id}: Delete a specified image

## Admin Management
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


## User Listings
* GET /users/{user_id}/properties: Get all properties listed by a specific user.


## Region, Area, City and Amenity
* GET /regions: Get a list of all regions.
* GET /regions/{region_id}: Get details of a specific region.
* GET /areas/{area_id}/: Get details of a specific area.
* GET /regions/{region_id}/areas: Get details of a specific area.

