from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


def generate_id() -> str:
    return str(uuid.uuid4())


## LOCATION
@dataclass
class Location:
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: Optional[str] = None
    pid: Optional[str] = None
    encoding_type: str = "application/geo+json"
    location: Optional['Geometry'] = None
    
    
## THING
@dataclass
class Thing:
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: Optional[str] = None
    pid: Optional[str] = None
    properties: Dict[str, Any] = field(default_factory=dict)

    location_id: List[str] = field(default_factory=list)

    
## SENSOR
@dataclass
class Sensor:
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: Optional[str] = None
    pid: Optional[str] = None
    encoding_type: str = "application/json"
    metadata: Optional[str] = None

    
## OBSERVEDPROPERTY
@dataclass
class ObservedProperty:
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: Optional[str] = None
    pid: Optional[str] = None
    definition: Optional[str] = None
    

## FEATURE OF INTEREST
@dataclass
class FeatureOfInterest:
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: Optional[str] = None
    pid: Optional[str] = None
    encoding_type: str = "application/geo+json"
    feature: Optional[Any] = None

    
## OBSERVATION
@dataclass
class Observation:
    id: str = field(default_factory=generate_id)
    phenomenon_time: datetime = field(default_factory=datetime.utcnow)
    result: float = 0.0
    result_time: Optional[datetime] = None
    result_quality: Optional[Dict[str, Any]] = None
    parameters: Optional[Dict[str, Any]] = None
    raw: Optional[Dict[str, Any]] = None
    time: Optional[datetime] = None

    datastream_id: Optional[str] = None
    feature_of_interest_id: Optional[str] = None

    
## DATASTREAM
@dataclass
class Datastream:
    id: str = field(default_factory=generate_id)
    name: str = ""
    description: Optional[str] = None
    pid: Optional[str] = None
    observation_type: str = "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement"
    unit_of_measurement: Dict[str, Any] = field(default_factory=dict)
    
    thing_id: Optional[str] = None
    sensor_id: Optional[str] = None
    observed_property_id: Optional[str] = None
