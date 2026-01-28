# BDOH Core - Domain and Schemas for IoT

# 1. Exporte les classes principales depuis domain/
from .domain import (
    Thing, Location, Sensor, ObservedProperty,
    Datastream, Observation, FeatureOfInterest
)

# 2. Exporte les schémas principaux depuis schemas/
from .schemas import (
    ThingCreate, ThingResponse, ThingUpdate,
    LocationCreate, LocationResponse, LocationUpdate,
    SensorCreate, SensorResponse, SensorUpdate,
    ObservedPropertyCreate, ObservedPropertyResponse, ObservedPropertyUpdate,
    DatastreamCreate, DatastreamResponse, DatastreamUpdate,
    ObservationCreate, ObservationResponse, ObservationUpdate,
    FeatureOfInterestCreate, FeatureOfInterestResponse, FeatureOfInterestUpdate
)

from .schemas import GeoJSONPoint, GeoJSONPolygon, UnitOfMeasurement
