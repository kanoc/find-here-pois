from httpx.client import Dispatcher
from httpx import Request, Response
from httpx.config import CertTypes, TimeoutTypes, VerifyTypes
from httpx.status_codes import codes

from tests import get_fixture_abspath


class MockDispatch(Dispatcher):
    """Network dispatcher for httpx that returns the given fixture file content instead of making a network call."""

    def __init__(self, filename: str = None):
        self.filename = filename

    async def send(self, request: Request, verify: VerifyTypes = None,
                   cert: CertTypes = None, timeout: TimeoutTypes = None) -> Response:
        if self.filename:
            with open(get_fixture_abspath(self.filename), 'rb') as fixture_file:
                content = fixture_file.read()
            return Response(codes.OK, content=content, request=request)
        return Response(codes.NOT_FOUND, request=request)
