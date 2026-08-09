from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
  nome: str = Field(min_length=3)
  idade: int = Field(ge=0)
  email: str = Field(max_length=100)


class UserResponse(BaseModel):
  id: int
  nome: str
  idade: int
  email: str
  data_cadastro: datetime

class UserPatch(BaseModel):
  nome: str
  idade: int
  email: str