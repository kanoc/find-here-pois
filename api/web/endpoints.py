from urllib.parse import urlencode
from typing import List, Dict, Union

from fastapi import APIRouter, Query, HTTPException
from starlette.responses import JSONResponse
import httpx

from api import config
from api.models import Hotel, BoundingBox, Message


router = APIRouter()

BASE_HERE_URL = 'https://places.sit.ls.hereapi.com/places/v1/'


@router.get("/healthcheck")
async def healthcheck() -> Dict:
    """Am I alive?"""

    return {"status": "Zed is *not* dead"}


@router.get("/api/hotels", response_model=List[Hotel], responses={424: {"model": Message}})
async def hotels(bbox_in: str = Query(None, title="Bounding Box", alias="bbox",
                                      regex=r"^\s*-?\d{1,3}(\.\d+)?,\s*-?\d{1,2}(\.\d+)?,"
                                            r"\s*-?\d{1,3}(\.\d+)?,\s*-?\d{1,2}(\.\d+)?\s*$",
                                      description="Search for hotels in this area, format: west longitude, "
                                                  "south latitude, east longitude, north latitude. "
                                                  "Example: 13.125,52.362,13.661,52.693"),
                 limit: int = 50):
    """Search for hotels in the given viewport (defined by a bounding box)."""

    # Do additional params parsing.
    bbox_params = [float(v.strip()) for v in bbox_in.split(',')]
    try:
        bbox = BoundingBox(west_lon=bbox_params[0], south_lat=bbox_params[1],
                           east_lon=bbox_params[2], north_lat=bbox_params[3])
    except ValueError as ve:
        # TODO: figure how to wrap custom pydantic validation errors into proper fastapi request errors
        raise HTTPException(400, str(ve))

    # Build and send the request.
    url_params: Dict[str, Union[str, int]] = {
        "apikey": config.HERE_REST_APP_API_KEY,
        "cat": "accommodation",
        "in": f"{bbox.west_lon},{bbox.south_lat},{bbox.east_lon},{bbox.north_lat}"
    }
    if limit > 0:
        url_params["size"] = limit

    url = f"discover/explore?{urlencode(url_params)}"
    headers = {
        "accept-encoding": "gzip"
    }
    async with httpx.Client(headers=headers, base_url=BASE_HERE_URL,
                            dispatch=config.HTTPX_CLIENT_DISPATCHER) as client:
        resp = await client.get(url)

    if resp.status_code != 200:
        # API call failed. Treat it as a "failed dependency" case.
        return JSONResponse(status_code=424, content={"message": str(resp.content)})

    # Interpret and transform the response.
    json_resp = resp.json()
    items = json_resp["results"].get("items", [])  # type: ignore
    if items:
        return [
            {
                "id": item["id"],
                "title": item["title"],
                "icon": item["icon"],
                "rating": item["averageRating"],
                "position": {
                    "lat": item["position"][0],
                    "lon": item["position"][1],
                }
            }
            for item in items
        ]

    # No items found.
    return []
