<h1>📦 Stock News Classifier</h1>

<p>한국 주식 뉴스의 호재/악재를 분류하는 AI 모델입니다.</p>

<hr>

<h2>🚀 설치 및 실행 방법</h2>

<h3>1. 저장소 클론</h3>

<pre><code>git clone https://github.com/jihyoung-lee/stock_news_classifier.git
cd stock_news_classifier
</code></pre>

<h3>2. 필수 패키지 설치</h3>

<pre><code>pip install -r requirements.txt
</code></pre>

<p><i>(※ transformers, torch, fastapi, uvicorn 등이 포함되어 있습니다.)</i></p>

<h3>3. 모델 다운로드 및 위치</h3>

<ul>
<li>모델 파일은 <code>model/my_model</code> 폴더에 저장되어 있어야 합니다.</li>
<li>이미 포함된 모델을 사용할 경우 추가 작업이 필요 없습니다.</li>
</ul>

<h3>4. 로컬 서버 실행</h3>

<pre><code>uvicorn app.main:app --reload
</code></pre>

<ul>
<li>서버가 정상적으로 실행되면 <code>http://localhost:8000/docs</code> 에서 API 테스트가 가능합니다.</li>
</ul>

<h3>5. API 사용법</h3>

<ul>
<li><b>GET /</b><br>서버 작동 확인용</li>
<li><b>POST /predict</b><br>입력 텍스트를 보내면 호재/악재 결과와 신뢰도를 반환합니다.</li>
</ul>

<h4>예시 요청</h4>

<pre><code>POST http://localhost:8000/predict

{
  "text": "삼성전자가 신제품을 출시했다."
}
</code></pre>

<h4>예시 응답</h4>

<pre><code>{
  "result": "호재",
  "confidence": 92.45
}
</code></pre>

<hr>

<h2>✨ 프로젝트 구성</h2>

<pre><code>app/
├── model_loader.py    # 모델 로딩
├── predictor.py       # 예측 함수
├── main.py            # FastAPI 서버
├── routes/            # API 엔드포인트
model/
└── my_model/          # 사전학습된 모델 및 토크나이저
</code></pre>

<hr>

<h2>⚡ 기타 주의사항</h2>

<ul>
<li>모델 경로(<code>model/my_model</code>)를 다른 곳으로 이동하면, <code>model_loader.py</code>에서 경로를 수정해야 합니다.</li>
<li>본 프로젝트는 CPU 환경에서도 동작할 수 있도록 최적화되어 있습니다.</li>
</ul>

<hr>
