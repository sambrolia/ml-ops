from typing import Optional
from pydantic import BaseModel, Field


class RequestItem(BaseModel):
    bed: int = Field(..., gt=0, lt=101, description="Number of bedrooms", example=3, error_messages={"gt": "Number of bedrooms must be greater than 0", "lt": "Number of bedrooms must be less than 101"})
    bath: float = Field(..., gt=0, lt=101, description="Number of bathrooms", example=2.5, error_messages={"gt": "Number of bathrooms must be greater than 0", "lt": "Number of bathrooms must be less than 101"})
    acre_lot: float = Field(..., ge=0, le=100000, description="Lot size in acres", example=1.5, error_messages={"ge": "Lot size must be greater than or equal to 0", "le": "Lot size must be less than or equal to 100000"})
    zip_code: int = Field(..., ge=10000, le=99999, description="Zip code", example=19720, error_messages={"ge": "Zip code must be greater than or equal to 10000", "le": "Zip code must be less than or equal to 99999"})
    house_size: int = Field(..., gt=0, lt=1000001, description="House size in square feet", example=2000, error_messages={"gt": "House size must be greater than 0", "lt": "House size must be less than 1000001"})

    class Config:
        schema_extra = {
            "example": {
                "bed": 3,
                "bath": 2.5,
                "acre_lot": 1.5,
                "zip_code": 19720,
                "house_size": 2000,
            }
        }
        extra = "forbid"
