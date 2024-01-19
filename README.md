# Sweets Vendors API

Welcome to the Sweets Vendors project! This is a Flask application that allows users to manage vendors, sweets, and their relationships.

## Features

With this application, you can:

- **View all vendors and sweets**: The application provides endpoints to retrieve a list of all vendors and sweets.

- **View a specific vendor or sweet**: You can retrieve detailed information about a specific vendor or sweet, including the associated vendor sweets.

- **Add a new vendor and sweet relationship**: The application allows you to create a new VendorSweet, which represents a specific sweet being sold by a specific vendor.

- **Delete an existing VendorSweet**: If needed, you can also delete an existing VendorSweet.

## Endpoints

The application provides the following endpoints:

- `GET /vendors`: Retrieve a list of all vendors.
- `GET /vendors/:id`: Retrieve detailed information about a specific vendor.
- `GET /sweets`: Retrieve a list of all sweets.
- `GET /sweets/:id`: Retrieve detailed information about a specific sweet.
- `POST /vendor_sweets`: Create a new VendorSweet relationship
- `DELETE /vendor_sweets/:id`: Delete an existing VendorSweet relationship.

**Installation**
1. Clone this repository 
    ```
    git clone git@github.com:kev065/p4-cc-sweets-vendors.git
    ```

2. Install dependencies with: 
    ```
    pipenv install
    ```

3. Navigate to the `app` directory and run the following commands: 
    ```
    $ export FLASK_APP=app.py
    $ export FLASK_RUN_PORT=5555
    $ flask run
    ```

4. The API will be available at: `http://127.0.0.1:5555`


## Usage
**Get all vendors**
```
http://127.0.0.1:5555/vendors
```
**Get a specific vendor**
```
http://127.0.0.1:5555/vendors/1
```

## License
This project is licensed under the terms of the [MIT Licence](https://github.com/kev065/p4-cc-sweets-vendors/blob/main/LICENSE/)
