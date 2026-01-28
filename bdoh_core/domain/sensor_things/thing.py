from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


## THING ___________
@dataclass
class Thing:
    id: Optional[int] = None
    pid: Optional[str] = None 
    name: str
    description: Optional[str] = None
    properties: Dict[str, Any] = field(default_factory=dict)
    locations: Set['Location'] = field(default_factory=set)
    datastreams: List['Datastream'] = field(default_factory=list)
