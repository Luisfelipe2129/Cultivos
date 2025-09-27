from pydantic import BaseModel

class CropData(BaseModel):
    n: int
    p: int
    k: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float