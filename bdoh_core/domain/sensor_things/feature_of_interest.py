from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


## FEATUREOFINTEREST _____________
@dataclass
class FeatureOfInterest:
    id: Optional[int] = None
    pid: Optional[str] = None 
    name: str
    description: Optional[str] = None
    encoding_type: str = "application/geo+json"
    feature: Optional[Any] = None  # Géométrie POLYGON
    observations: List['Observation'] = field(default_factory=list)
