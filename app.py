from fastapi import FastAPI
from pydantic import BaseModel
import pickle

from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-base")

app = FastAPI()


@app.get('/RAG')
def ask(prompt: str):
    result = pipe(prompt)
    return result[0]


class ModelInput(BaseModel):
    pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
        
# Load the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.post('/Classification')
def diabetes_pred(input_parameters: ModelInput):
    input_list = [
        input_parameters.pregnancies, 
        input_parameters.Glucose, 
        input_parameters.BloodPressure, 
        input_parameters.SkinThickness, 
        input_parameters.Insulin, 
        input_parameters.BMI, 
        input_parameters.DiabetesPedigreeFunction, 
        input_parameters.Age
    ]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return {'prediction': 'The person is not diabetic'}
    else:
        return {'prediction': 'The person is diabetic'}
