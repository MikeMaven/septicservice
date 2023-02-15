# Septic Service API

This Django project provides a simple API for retrieving septic information based on address.

## API Endpoint

The API endpoint is located at `/septic-info/<address>/` and accepts a GET request with an address parameter. It returns septic information for the specified address in JSON format.

Example: `http://localhost:8000/septic-info/123%20Main%20St/`

## Running the Project

To run the project, make sure you have Django installed and run the following command in your terminal or command prompt:

`python manage.py runserver`


The server will start on `http://localhost:8000/`.

## Dependencies

This project requires Django 3.2 or higher.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
