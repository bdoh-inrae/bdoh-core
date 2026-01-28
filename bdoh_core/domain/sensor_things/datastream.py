from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


# Datastream ________________
@dataclass
class Datastream:
    id: Optional[int] = None
    pid: Optional[str] = None 
    name: str
    description: Optional[str] = None
    observation_type: str = "http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement"
    unit_of_measurement: Dict[str, Any] = field(default_factory=dict)
    
    # Foreign keys (optionnels dans le domaine)
    thing_id: Optional[str] = None
    sensor_id: Optional[str] = None
    observed_property_id: Optional[str] = None
    
    # Relationships (optionnelles)
    thing: Optional[Thing] = None
    sensor: Optional[Sensor] = None
    observed_property: Optional[ObservedProperty] = None
    observations: List['Observation'] = field(default_factory=list)
