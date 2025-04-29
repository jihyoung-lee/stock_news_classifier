import torch


def predict(text, model, tokenizer):
    model.eval()  # 모델을 evaluation 모드로 전환
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512,
    )
    with torch.no_grad():  # 역전파 끔
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=-1)

        # 가장 확률 높은 클래스 번호 가져오기
        prediction = torch.argmax(probs, dim=-1).item()

        # 가장 높은 확률값 가져오기
        confidence = torch.max(probs, dim=-1)[0].item()

    return prediction, confidence