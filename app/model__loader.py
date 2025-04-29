from transformers import BertTokenizer, BertForSequenceClassification
import os
import zipfile
zip_path = "app/model.zip"
model_path = "model/my_model"

# 모델 폴더가 비어있으면 압축 해제
if not os.path.exists(os.path.join(model_path, "model.safetensors")):
    print("모델 파일이 없어 압축을 풉니다...")

    # 폴더 없으면 생성
    os.makedirs(model_path, exist_ok=True)

    # 압축 풀기
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(model_path)

    print("압축 해제 완료")
else:
    print("모델 파일이 이미 존재합니다. 압축 해제 생략.")

def get_model():
    # 모델 불러오기
    model = BertForSequenceClassification.from_pretrained(model_path,
                                                          local_files_only=True,
                                                          )
    tokenizer = BertTokenizer.from_pretrained(model_path,
                                              local_files_only=True,
                                              )
    return model, tokenizer