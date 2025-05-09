<h1>📦 Stock News Classifier</h1>

<p>This is an AI model that classifies South Korean stock market news into positive or negative sentiment categories.</p>
<hr>

<p align="center">
  <img src="https://github.com/user-attachments/assets/3d2ae08f-61ff-4999-bc98-f9ecad924688" width="600"/>
  <img src="https://github.com/user-attachments/assets/108c01b4-d0e8-4462-8d0d-d51ca1710333" width="600"/>
</p>


## 📊 Training Summary

This project was designed to fine-tune the `klue/bert-base` model on a small-scale Korean text classification dataset (700 samples).  
To prevent overfitting and improve generalization, the lower layers of BERT (embeddings and first 2 encoder blocks) were frozen during training.

### ⚙️ Configuration
- **Pretrained model**: `klue/bert-base`
- **Train samples**: ~700
- **Epochs**: 3
- **Batch size**: 8
- **Learning rate**: 1e-5
- **Frozen layers**: embeddings + encoder.layer.0~1
- **Early stopping**: Enabled (patience=1)

---

### 🏋️ Training Metrics
- **Training steps**: 216  
- **Training loss**: `0.5033`  
- **Training runtime**: `94.28s`  
- **Samples/sec**: `18.20`  
- **Steps/sec**: `2.29`  

---

### ✅ Evaluation Results
- **Evaluation loss**: `0.4455`  
- **Accuracy**: `79.17%`  
- **Precision**: `79.33%`  
- **Recall**: `78.13%`  
- **F1 Score**: `78.46%`  
- **Evaluation runtime**: `0.49s`  

---

## 📌 Notes

- The training remained stable across all 3 epochs without signs of severe overfitting.
- Evaluation scores indicate a balanced performance, considering the small dataset size.
---

## Dataset

- Approximately 700 samples were manually collected and labeled.
- The dataset was built by crawling news headlines related to stock market trends (positive/negative sentiment).
- Data collection, labeling, and preprocessing were entirely self-performed to ensure data quality and relevance.

The dataset consists of approximately 700 manually collected and labeled news headlines, focusing on stock market sentiment (positive or negative). All data collection and preprocessing processes were performed independently.


<h2>🚀 Installation & Execution</h2>

<h3>1. Clone the Repository</h3>

<pre><code>git clone https://github.com/jihyoung-lee/stock_news_classifier.git
cd stock_news_classifier
</code></pre>

<h3>2. Install Required Packages</h3>

<pre><code>pip install -r requirements.txt
</code></pre>

<p><i>(Includes transformers, torch, fastapi, uvicorn, and more.)</i></p>

<h3>3. Download and Place Model</h3>

<ul>
<li>The model files should be located in the <code>model/my_model</code> directory.</li>
<li>If you're using the pre-included model, no additional setup is needed.</li>
</ul>

<h3>4. Run the Local Server</h3>

<pre><code>uvicorn app.main:app --reload
</code></pre>

<ul>
<li>If the server runs successfully, you can test the API at <code>http://localhost:8000/docs</code>.</li>
</ul>

<h3>5. API Endpoints</h3>

<ul>
<li><b>GET /</b><br>Health check endpoint</li>
<li><b>POST /predict</b><br>Sends input text and returns a prediction (positive/negative) with confidence score.</li>
</ul>

<h4>Example Request</h4>

<pre><code>POST http://localhost:8000/predict

{
  "text": "삼성전자 주가 상승"
}
</code></pre>

<h4>Example Response</h4>

<pre><code>{
  "result": "긍정",
  "confidence": 92.45
}
</code></pre>

<hr>

<h2>✨ Project Structure</h2>

<pre><code>app/
├── model_loader.py    # Loads the model
├── predictor.py       # Prediction logic
├── main.py            # FastAPI server
├── routes/            # API routes
model/
└── my_model/          # Pretrained model and tokenizer
</code></pre>

<hr>

<h2>⚡ Notes</h2>
<ul>
<li>If you move the model directory (<code>model/my_model</code>), be sure to update the path in <code>model_loader.py</code>.</li>
<li>The model files can be downloaded <a href="https://drive.google.com/drive/folders/1uB28sLJQ7x8M0lm47SjiZEPLRSHSEA92?usp=sharing" target="_blank">here</a>.</li>
</ul>

<hr>
