# Septic Service Information API

This Django project provides a simple API for retrieving septic information based on street address and zip code.
It returns a boolean value to be leveraged by our application that extracts away the implementation of the 3rd party API it uses to retrieve the information.

## API Endpoint

The API endpoint is located at `/septic-info/<address>/<zip_code>` and accepts a GET request with an address parameter. It returns septic information for the specified address in JSON format.

Example: `http://localhost:8000/septic-info/123%20Main%20St/02920`

## Running the Project

To run the project, make sure you have Django installed and run the following command in your terminal or command prompt:

`python manage.py runserver`


The server will start on `http://localhost:8000/`.

## Dependencies

This project requires Django 3.2 or higher.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
