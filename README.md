# Septic Service Information API

This Django project provides a simple API for retrieving septic information based on street address and zip code.
It returns a boolean value to be leveraged by our application that extracts away the implementation of the 3rd party API it uses to retrieve the information.
The boolean value is meant to signify whether or not the API returns information signaling that the home does have a septic system, which the front end can then
leverage to ask the additional question related to septics.

Since the customer facing piece of this application is part of a customer flow prior to account creation, and therefore there is no authenitcated user present,
I would opt for a security implementation that is handled by a proxy - namely in the form of API Gateway / APIM. In the cloud deployment of this microservice,
a security group would be added to configure inbound traffic as only being allowed to come from the API Gateway, and security, including application subscriptions, would be
handled by the proxy.

To address scalability, I've included a basic Dockerfile so the application can be deployed to Amazon ECS.

## API Endpoint

The API endpoint is located at `/septic-info/<address>/<zip_code>` and accepts a GET request with an address parameter. It returns septic information for the specified address in JSON format.

Example: `http://localhost:8000/septic-info/123%20Main%20St/02920`

In order to leverage the HouseCanary API, an environment variable of `HOUSECANARY_API_KEY` must be present in the deployment environment.

## Running the Project

To run the project, make sure you have Django installed and run the following command in your terminal or command prompt:

`python manage.py runserver`

## Running Tests: HouseCanary API is restricted to organizations with paid access

Because HouseCanary is not a free, open API, the API has been mocked in a series of unit tests.

To run the tests, run the following command:

`python manage.py test`


The server will start on `http://localhost:8000/`.

## Dependencies

This project requires Django 3.2 or higher.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
