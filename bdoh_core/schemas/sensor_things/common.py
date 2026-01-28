from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List


## COMMON ____________________
class GeoJSONPoint(BaseModel):
    """Schéma pour un point GeoJSON"""
    type: str = "Point"
    coordinates: list[float]  # [longitude, latitude]

class GeoJSONPolygon(BaseModel):
    """Schéma pour un polygone GeoJSON"""
    type: str = "Polygon"
    coordinates: list[list[list[float]]]  # [[[lng, lat], ...]]

class UnitOfMeasurement(BaseModel):
    """Schéma pour unitOfMeasurement standardisé"""
    name: str
    symbol: str
    definition: Optional[str] = None

