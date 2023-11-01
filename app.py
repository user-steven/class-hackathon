from flask import Flask, request
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/analyze')
def analyse():
    sentence = request.args.get('sentence')
    print(sentiment_pipeline(sentence))
    result = sentiment_pipeline(sentence)
    return(result)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)