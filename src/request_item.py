from pydantic import BaseModel

class RequestItem(BaseModel):

    bed: int = None
    bath: int = None
    acre_lot: float = None
    zip_code: int = None
    house_size: int = None

    class Config:
        schema_extra = {
            "example": {
                "bed": 3,
                "bath": "2",
                "acre_lot": 1.5,
                "zip_code": "19720",
                "house_size": 2000,
            }
        }