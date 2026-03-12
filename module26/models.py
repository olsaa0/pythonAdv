from pydantic import BaseModel
from typing import Optional
from typing import Union
from typing import Any
from typing import List

class Recipe(BaseModel):
    id: Optional[int] = None
    name: str
    category: str
    ingredients: List[str]
    instructions: Optional[str] = None

class RecipeUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]
    ingredients: Optional[List[str]]
    instructions: Optional[str]

class AnyData(BaseModel):
    data: Union[str, int, float, List[Any]]



