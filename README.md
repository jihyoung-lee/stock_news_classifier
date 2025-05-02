<h1>📦 Stock News Classifier</h1>

<p>This is an AI model that classifies South Korean stock market news into positive or negative sentiment categories.</p>
<hr>

<p align="center">
  <img src="https://github.com/user-attachments/assets/bbbf5f05-9981-439e-ba68-81cc5b96dd30" width="600"/>
</p>


## Training Summary

- **Training steps**: 360
- **Training loss**: 0.2370
- **Training runtime**: 329.5 seconds
- **Samples per second**: 8.68
- **Steps per second**: 1.093
- **Epochs**: 5

## Evaluation Results

- **Evaluation loss**: 0.4477
- **Accuracy**: 90.97%
- **Precision**: 91.64%
- **Recall**: 90.21%
- **F1 Score**: 90.69%
- **Evaluation runtime**: 4.03 seconds
This project achieved a training loss of 0.2370 and an evaluation accuracy of approximately 91% after 5 epochs, demonstrating stable training and strong performance on the validation dataset.

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
<li>The model files can be downloaded <a href="https://drive.google.com/file/d/1JVIVQMkJw1ZV0p4XmXJZTZDX4_VhjWKz/view?usp=sharing" target="_blank">here</a>.</li>
</ul>

<hr>
