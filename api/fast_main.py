import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_sentiment
from database_api import save_text_to_db
from databases.update_csv import updated_csv

app = FastAPI()

SENTIMENT_MAP = {1: "positive", 0: "neutral", 2: "negative"}

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    sentiment: str

@app.post("/predict/", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    sentiment = predict_sentiment(request.text)  
    sentiment_label = SENTIMENT_MAP.get(sentiment, "unknown")  
    
    save_text_to_db(request.text, sentiment_label)  
    updated_csv()  
    
    return SentimentResponse(text=request.text, sentiment=sentiment_label)
