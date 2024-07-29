from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np
import pandas as pd
# Charger le modèle
#model = pickle.load(open('churn_model.pkl', 'rb'))
model = load('churn_model.joblib')
app = FastAPI()

# Définir la structure des données d'entrée
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.post('/predict')
def predict_churn(data: CustomerData):
    # Convertir les données en dataframe
    data_dict = data.model_dump()
    df = pd.DataFrame([data_dict])

    # Prédiction
    prediction = model.predict(df)
    prediction_proba = model.predict_proba(df)

    return {
        'prediction': int(prediction[0]),
        'probability': float(prediction_proba[0][1])
    }
