from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


## SENSOR ______________
@dataclass
class Sensor:
    id: Optional[int] = None
    pid: Optional[str] = None 
    name: str
    description: Optional[str] = None
    encoding_type: str = "application/json"
    metadata: Optional[str] = None  # Text dans l'ORM, str ici
    datastreams: List['Datastream'] = field(default_factory=list)
