# EveryBar server #

Welcome to the EveryBar server! This server is built using Flask and serves as the backend for the Nightlife Finder mobile application. It provides API endpoints for managing users and businesses and interacts with a MongoDB database.

## Features ##

- Add User: Add a new user to the database.
- Get User: Retrieve user information based on user ID.
- Add Business: Add a new nightlife business to the database, including images.
- Get All Businesses: Retrieve a list of all businesses with their details and images.


# API Endpoints #
## Add User ##
- Endpoint: /add_user
- Method: POST

## Get User ##
- Endpoint: /get_user
- Method: GET
- Query Parameter: uid (user ID)

## Add Business ##
- Endpoint: /add_business
- Method: POST

## Get All Businesses ##
Endpoint: /get_all_businesses

Method: GET
