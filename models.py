from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Customer(BaseModel):
     customer_id: Optional[UUID] = uuid4()
     first_name: str
     last_name: str
     phone: str
     city:str
     state:str
     postcode : str
     email:str



class CustomerUpdate(BaseModel):
     customer_id: Optional[UUID] = uuid4()
     first_name: Optional[str]
     last_name: Optional[str]
     phone: Optional[str]
     city: Optional[str]
     state: Optional [str]
     postcode :Optional [str]
     email: Optional[str]

      
    