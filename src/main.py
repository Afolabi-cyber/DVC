from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

app = FastAPI(
    title= "Water Portability Predictiion",
    description = 'Predicting water portability'
)

with open('C:/Users/user/Documents/DVC/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.get("/")
def index():
    return "Welcome to water portability prediction FASTAPI"

@app.post("/prediction")
def model_prediction(water: Water):
    pd.DataFrame({
        'ph' : [water.ph],
        "hardness": [water.hardness],
        "Solids": [water.Solids],
        "Chloramines" : [water.Chloramines],
        "Sulfate": [water.Sulfate],
        "Conductivity": [water.Conductivity],
        "Organic_carbons": [water.Organic_carbons],
        "Trihalomethanses": [water.Trihalomethanses],
        "Turbidity": [water.Turbidity]
    })