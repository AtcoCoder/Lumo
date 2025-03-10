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

___


### POST /auth/login: Log in an existing user.
#### Parameters
***email*** `string`

[required] user's email address

***password*** `string`

[required] user's password

#### Example request body
```json
{
    "email": "john@email.com",
    "password": "password"
}
```

#### Example request body
```json
{
    "access_token": "[your_token]",
    "refresh_token": "[your_refresh_token]"
}
```

___


### GET /auth/logout: Log out the user.
#### Headers
***Authentication*** `Bearer Token`

#### Example request header
```json
{
    "authorization": "Bearer [your_token]"
}
```
#### successful response status code: `200`

___

### GET /users/me: Get the currently authenticated user's details.
#### Headers
***Authentication*** `Bearer Token`

#### Example request header
```json
{
    "authorization": "Bearer [your_token]"
}
```

#### Example response
```json
{
    "me": {
        "__class__": "User",
        "created_at": "2025-01-21T18:29:59",
        "email": "john@email.com",
        "id": "a0106dc7-cbae-4118-a879-648fbd4e6b15",
        "phone_number": "12345609",
        "properties": [],
        "updated_at": "2025-01-21T18:29:59",
        "username": "john",
        "whatsapp": "12345609"
    }
}
```

___

### PATCH /users/me: Update the currently authenticated user's profile
#### Parameters
***username*** `string`
[optional] new username of user

***email*** `string`
[optional] new email address of user

***phone_number*** `string`
[optional] new phone number

***whatsapp*** `string`
[optional] new whatsapp number

***password*** `string`
[optional] new password

#### Headers
***Authentication*** `Bearer Token`

#### Example request header
```json
{
    "authorization": "Bearer [your_token]"
}
```

#### Example request body
```json
{
    "username": "new_username",
    "email": "new_email",
    "phone_number": "1349874",
    "whatsapp": "1349874",
    "password": "new_password"
}
```

#### Example response
```json
{
    "message": ""
}
```


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

