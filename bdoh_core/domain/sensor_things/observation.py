from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Set
from datetime import datetime
import uuid


# Observation ____________
@dataclass
class Observation:
    id: Optional[int] = None
    pid: Optional[str] = None 
    datastream_id: str
    phenomenon_time: datetime
    result: float
    result_time: Optional[datetime] = None
    result_quality: Optional[Dict[str, Any]] = None
    parameters: Optional[Dict[str, Any]] = None
    feature_of_interest_id: Optional[str] = None
    raw: Optional[Dict[str, Any]] = None
    
    # Pour compatibilité avec ton modèle existant
    time: Optional[datetime] = None  # Sera égal à phenomenon_time
    
    # Relationships (optionnelles)
    datastream: Optional[Datastream] = None
    feature_of_interest: Optional[FeatureOfInterest] = None
