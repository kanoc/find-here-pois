from starlette.testclient import TestClient

from api.web import app


client = TestClient(app)
