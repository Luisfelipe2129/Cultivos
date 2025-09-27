from datetime import date
from fastapi import APIRouter

from services.cultivos_service import cultivos_prediction
from schemas.cultivos_schemas import CropData

router = APIRouter()

@router.post("/predict")
async def patient_predict(data: CropData):
    
    prediction = cultivos_prediction(data)
    return {"prediccion:": prediction}
