# weather-api 

Use this api project to get weather information for most of the cities around the world

## Dependencies

- To run this project you must need to have [Docker](https://docs.docker.com/engine/install/) installed

## Running this project locally

- Clone or download the repo

- look for the `example.env` file located in the root directory and make the following steps:

    1. Open the file and **put the corresponding values to each environment variables**. You must have received them in yor email.

    2. Save the file changes and close it

    3. Change the file name from `example.env` to `.env`

- Open a terminal in the root directory

- run the following command line:

    ```bash
    docker build -t weather_api . && docker run -p 8000:8080 -d weather_api
    ```

## Usage

- Open your browser or any `http client` to make a `GET` request

- Once the project is running use the `url` below to build your request:

    ```url
    http://localhost:8080/?city=<city>&country=<iso_2_country_code>
    ```

    - `city` is the name of the city, you can put spaces between. example: *Valledupar*

    - `iso_2_country_code` is a country code of two characters in lowercase. example: *co*

- Paste the `url` in your client/browser and make the request. Example: `http://localhost:8000/?city=lima&country=pe`




## Author

Camilo Henao Álvarez

Globant technical test

June - 2023