#!/usr/bin/env python
from enum import Enum
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

import joblib
import os
import pandas as pd

# create the app
app = FastAPI()

# Load the model
model_path = os.path.join(".", "randomforest.joblib")
rf_model = joblib.load(model_path)

# Input body for validation
class CategoryEnum(Enum):
    one_dish = "One Dish Meal"
    lunck = "Lunch/Snacks"
    breakfast = "Breakfast"
    dessert = "Dessert"
    meat = "Meat"
    chicken = "Chicken"
    port = "Pork"
    beverages = "Beverages"
    vegetable = "Vegetable"
    potato = "Potato"

class Body(BaseModel):
    calories: float
    carbohydrates: float
    sugar: float
    protein: float
    category: CategoryEnum
    servings: int

# Expose endpoints
@app.get('/', response_class=HTMLResponse)
def root():
    """Endpoint for the landing page"""
    return HTMLResponse("<h1>A self-documenting API to interact with a recipie prediction model</h1>")

@app.post('/predict', response_class=JSONResponse)
def generate_recipes(body: Body):
    """Predict if the recipie will generate high traffic"""
    try:
        formatted_input = {
            "calories": body.calories,
            "carbohydrate": body.carbohydrates,
            "sugar": body.sugar,
            "protein": body.protein,
            "category": body.category.value,
            "servings": body.servings
        }
        df_input = pd.DataFrame.from_dict([formatted_input])

        result = rf_model.predict(df_input).tolist()
    except Exception as traffic_prediction_error:
        error_msg = f"Error predicting recipe traffic: {traffic_prediction_error}"
        raise HTTPException(status_code=500, detail=error_msg)
    
    return {"prediction": result}