import pytest

from tests.web import client


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "Zed is *not* dead"}


@pytest.mark.parametrize("mock_httpx_dispatcher, hotel_count", [
                            ("two_hotels.json", 2),
                            ("no_hotels.json", 0)
                         ], indirect=["mock_httpx_dispatcher"])
def test_hotels(mock_httpx_dispatcher, hotel_count):
    response = client.get("/api/hotels?bbox=13.125,52.362,13.661,52.693&limit=2")
    assert response.status_code == 200
    json = response.json()
    assert len(json) == hotel_count


@pytest.mark.parametrize("mock_httpx_dispatcher, status_code", [
                            ("", 424),  # Missing filename triggers a 404 in the dispatcher
                         ], indirect=["mock_httpx_dispatcher"])
def test_hotels_failed_dependency(mock_httpx_dispatcher, status_code):
    response = client.get(f"/api/hotels?bbox=13.125,52.362,13.661,52.693&limit=2")
    assert response.status_code == status_code


@pytest.mark.parametrize("bbox, limit, status_code", [
                             ("13.125,52.362,13.661,52.693", "4m", 422),  # Invalid limit
                             ("13.12552.362,13.661,52.693", "4", 422),  # Invalid bbox format
                             ("230.125,52.362,13.661,52.693", "4", 400),  # Invalid lon
                             ("13.125,95.362,13.661,52.693", "4", 400),  # Invalid lat
                         ])
def test_hotels_invalid_params(bbox, limit, status_code):
    response = client.get(f"/api/hotels?bbox={bbox}&limit={limit}")
    assert response.status_code == status_code


def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200
