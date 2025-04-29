from fastapi import FastAPI
from pydantic import BaseModel
from app.model__loader import get_model
from app.predictor import predict
app = FastAPI()

# load model and tokenizer
model, tokenizer = get_model()

# 요청 형식 정의
class InputText(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Api is working"}

@app.post("/predict")
async def predict_route(inputText: InputText):
    prediction, confidence = predict(inputText.text, model, tokenizer)

    label = "호재" if prediction == 1 else "악재"
    # %로 출력
    return {
            "result": label,
            "confidence": round(confidence * 100, 2),
    }