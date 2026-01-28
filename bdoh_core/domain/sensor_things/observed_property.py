from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


## OBSERVEDPROPERTY ______________
@dataclass
class ObservedProperty:
    id: Optional[int] = None
    pid: Optional[str] = None 
    name: str
    description: Optional[str] = None
    definition: Optional[str] = None
    datastreams: List['Datastream'] = field(default_factory=list)
