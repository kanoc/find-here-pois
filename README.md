## Required packages

Make sure you have installed:
 * ``docker`` (tested with v18.09.7)
 * ``docker-compose`` (tested with v1.17.1)

## Usage

1. Fire it up the services
```bash
$ docker-compose up -d
```

2. Browse to `localhost:3000` to interact with the client.

3. Browse to `localhost:9000/redoc` or `localhost:9000/docs` for the API docs.

4. Follow the logs across all running services
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