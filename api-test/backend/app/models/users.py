from typing import Literal
from pydantic import BaseModel, EmailStr, Field, model_validator

class UserBaseSchema(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=40, examples=['John'])
    last_name: str = Field(..., min_length=2, max_length=40, examples=['Doe'])
    email: EmailStr
    age: int
    status: Literal['active', 'inactive']
    gender: Literal['male', 'female', 'mayo']
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Pudge",
                    "last_name": "Bloodhooker",
                    "email": "mrpudge@valve.com",
                    "age": 69,
                    "status": "active",
                    "gender": "male"
                }
            ]
        }
    }
    
    @model_validator(mode="after")
    def validate_positive_fields(self):
        fields = ['age']
        
        for field in fields:
            value = getattr(self, field)
            
            if value <= 0:
                raise ValueError(f"{field} must be a positive number")
        
        return self
    
class UserSchema(UserBaseSchema):
    id: int
   
