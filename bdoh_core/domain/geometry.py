from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class Geometry:
    type: str = field(init=False) 
    coordinates: Any
    
    def to_geojson(self) -> dict:
        return {"type": self.type, "coordinates": self.coordinates}


@dataclass
class Point(Geometry):
    def __post_init__(self):
        self.type = "Point"
        if not (isinstance(self.coordinates, list) and len(self.coordinates) == 2):
            raise ValueError("Point coordinates must be [lon, lat]")


@dataclass
class MultiPoint(Geometry):
    def __post_init__(self):
        self.type = "MultiPoint"
        if not (isinstance(self.coordinates, list) and all(isinstance(p, list) and len(p) == 2 for p in self.coordinates)):
            raise ValueError("MultiPoint coordinates must be list of [lon, lat] points")


@dataclass
class LineString(Geometry):
    def __post_init__(self):
        self.type = "LineString"
        if not (isinstance(self.coordinates, list) and all(isinstance(p, list) and len(p) == 2 for p in self.coordinates)):
            raise ValueError("LineString coordinates must be list of [lon, lat] points")


@dataclass
class MultiLineString(Geometry):
    def __post_init__(self):
        self.type = "MultiLineString"
        if not (isinstance(self.coordinates, list) and all(isinstance(line, list) and all(isinstance(p, list) and len(p) == 2 for p in line) for line in self.coordinates)):
            raise ValueError("MultiLineString coordinates must be list of LineStrings")


@dataclass
class Polygon(Geometry):
    def __post_init__(self):
        self.type = "Polygon"
        if not (isinstance(self.coordinates, list) and all(isinstance(ring, list) and all(isinstance(p, list) and len(p) == 2 for p in ring) for ring in self.coordinates)):
            raise ValueError("Polygon coordinates must be list of linear rings")


@dataclass
class MultiPolygon(Geometry):
    def __post_init__(self):
        self.type = "MultiPolygon"
        if not (isinstance(self.coordinates, list) and all(isinstance(polygon, list) and all(isinstance(ring, list) and all(isinstance(coord, list) and len(coord) == 2 for coord in ring) for ring in polygon) for polygon in self.coordinates)):
            raise ValueError("MultiPolygon coordinates must be list of polygons")


@dataclass
class GeometryCollection(Geometry):
    geometries: List[Geometry] = field(default_factory=list)

    def __post_init__(self):
        self.type = "GeometryCollection"
        if not isinstance(self.geometries, list) or not all(isinstance(g, Geometry) for g in self.geometries):
            raise ValueError("GeometryCollection must contain a list of Geometry objects")
        self.coordinates = None
