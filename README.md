## Required packages

Make sure you have installed:
 * ``docker`` (tested with v18.09.7)
 * ``docker-compose`` (tested with v1.17.1)
 * ``git`` (tested with v2.17.1)

## Clone the repo

```bash
git clone --recurse-submodules https://github.com/kanoc/find-here-pois.git
```

## Demo

* Client: https://find-here-pois-client.herokuapp.com/
* API: https://find-here-pois-api.herokuapp.com/redoc or https://find-here-pois-api.herokuapp.com/docs

**Note**: Both the client and API are running on free tier dynos (are shut down automatically if not used for 30 min),
hence it might take up to 20 seconds until they get fired up on first access.

## Usage

1. Create an `.env` file (in the repo root folder) containing
```.env
HERE_REST_APP_API_KEY=your-here-rest-api-key
```

2. Fire it up the services
```bash
$ docker-compose up -d
```

3. Browse to `localhost:3000` to interact with the client.

4. Browse to `localhost:9000/redoc` or `localhost:9000/docs` for the API docs.

5. Follow the logs across all running services
```bash
$ docker-compose logs -f
```

## Tests

To run the tests in a virtual env:
1. Create a virtual env with `virtualenv`:
   ```bash
   mkvirtualenv -p /usr/bin/python3.7 find-here-pois
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Code quality checks:
```bash
inv check
```

Run the tests:
1. Install the dev requirements with:
    ```bash
    inv deps
    ```
2. Run the tests with coverage report:
    ```bash
    inv test
    ```
3. Run the tests without coverage report:
    ```bash
    inv test --no-coverage
    ```
