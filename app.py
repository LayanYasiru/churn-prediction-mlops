import os
import sys
import uvicorn
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ROOT_DIR, 'src'))
from model_inference import ModelInference

app = FastAPI(title="Churn Prediction API", version="1.0.0")

inference_system = ModelInference(model_path='artifacts/models/churn_analysis.joblib')

class CustomerData(BaseModel):
    RowNumber: int = Field(..., example=1)
    CustomerId: int = Field(..., example=15634602)
    Firstname: str = Field(..., example="Yasiru")
    Lastname: str = Field(..., example="Liyanage")
    CreditScore: int = Field(..., example=619)
    Geography: str = Field(..., example="France") # France, Germany, Spain
    Gender: str = Field(..., example="Female")    # Female, Male
    Age: int = Field(..., example=42)
    Tenure: int = Field(..., example=2)
    Balance: float = Field(..., example=0.0)
    NumOfProducts: int = Field(..., example=1)
    HasCrCard: int = Field(..., example=1)
    IsActiveMember: int = Field(..., example=1)
    EstimatedSalary: float = Field(..., example=101348.88)

@app.get("/")
def home():
    return {"message": "Churn Prediction API is Online. Go to /docs"}

@app.post("/predict")
async def predict(data: CustomerData):
    try:
        input_data = data.model_dump()
        
        input_data['Gender_Female'] = 1 if input_data['Gender'] == 'Female' else 0
        input_data['Gender_Male'] = 1 if input_data['Gender'] == 'Male' else 0

        input_data['Geography_France'] = 1 if input_data['Geography'] == 'France' else 0
        input_data['Geography_Germany'] = 1 if input_data['Geography'] == 'Germany' else 0
        input_data['Geography_Spain'] = 1 if input_data['Geography'] == 'Spain' else 0

        result = inference_system.predict(input_data)

        return {
            "Gender Female":input_data['Gender_Female'],
            "Gender Male":input_data['Gender_Female']  ,
            "customer_id": data.CustomerId,
            "prediction": result['Status'],
            "confidence": result['Confidence']
        }

    except Exception as e:
        print(f"PREDICTION ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)