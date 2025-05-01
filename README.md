<h1>📦 Stock News Classifier</h1>

<p>This is an AI model that classifies South Korean stock market news into positive or negative sentiment categories.</p>

<hr>

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
  "text": "Samsung Electronics has launched a new product."
}
</code></pre>

<h4>Example Response</h4>

<pre><code>{
  "result": "Positive",
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
