from pydantic import BaseModel
from typing import List , Optional

class Resume(BaseModel):
    candidate_name: str
    email : str
    skills : List[str]
    experience :Optional[int]  =0 
    education : str
