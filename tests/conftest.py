import pytest

from api import config

from tests.utils import MockDispatch


@pytest.fixture
def mock_httpx_dispatcher(request, monkeypatch):
    """Set `api.config.HTTPX_CLIENT_DISPATCHER` to a mock that returns a fixture file."""

    monkeypatch.setattr(config, "HTTPX_CLIENT_DISPATCHER", MockDispatch(request.param))
