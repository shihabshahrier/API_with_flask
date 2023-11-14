# Flask User Management API

This project is a simple Flask-based user management system, providing a REST API to create, retrieve, and update user information using a SQLite database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- pip (Python package manager) installed.

## Installing Flask User Management API

To install Flask User Management API, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/shihabshahrier/API_with_flask.git
   cd API_with_flask
    ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, follow these steps:

1. Run the application:
   ```bash
   python3 app.py
   ```

## Using the API

The API supports the following endpoints:

- GET /get-user/<username>: Retrieve a user by username.
- POST /add-user: Add a new user. The request should include username and email in the JSON body.
- PUT /update/<username>: Update an existing user's email. The request should include email in the JSON body.
