from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


## LOCATION ___________
@dataclass
class Location:
    id: Optional[int] = None
    pid: Optional[str] = None 
    name: str
    description: Optional[str] = None
    encoding_type: str = "application/geo+json"
    location: Optional[Any] = None  # Géométrie (tu pourras typer plus précisément plus tard)
    things: Set['Thing'] = field(default_factory=set)

