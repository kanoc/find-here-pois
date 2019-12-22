from pydantic import BaseModel, validator


class LatLon(BaseModel):
    lat: float
    lon: float


class Hotel(BaseModel):
    id: str
    title: str
    icon: str
    rating: int
    position: LatLon


class BoundingBox(BaseModel):
    west_lon: float
    south_lat: float
    east_lon: float
    north_lat: float

    @validator('west_lon', 'east_lon')
    def check_lon(cls, v):
        if v < -180 or v > 180:
            raise ValueError('Longitude must within -180 and 180 degrees!')
        return v

    @validator('south_lat', 'north_lat')
    def check_lat(cls, v):
        if v < -90 or v > 90:
            raise ValueError('Latitude must within -90 and 90 degrees!')
        return v


class Message(BaseModel):
    message: str
