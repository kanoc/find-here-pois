import os
from typing import Optional

from httpx.client import Dispatcher

HERE_REST_APP_API_KEY = os.environ["HERE_REST_APP_API_KEY"]
HTTPX_CLIENT_DISPATCHER: Optional[Dispatcher] = None  # Makes it easier to mock httpx network requests in tests
