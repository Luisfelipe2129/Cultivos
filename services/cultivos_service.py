

import pickle

import numpy as np
from schemas.cultivos_schemas import CropData

with open('cultivos.pkl', 'rb') as file:
    model = pickle.load(file)


def cultivos_prediction(data: CropData):

    xin=np.array([
   
    data.n,
    data.p,
    data.k,
    data.temperature,
    data.humidity,
    data.ph,
    data.rainfall,
   

    ]).reshape(1,-1)


    prediction = model.predict(xin)


    
    return prediction[0]