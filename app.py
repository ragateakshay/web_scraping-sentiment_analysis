from flask import Flask, render_template, request
import requests
import nltk
from newspaper import Article
import textblob
from textblob import TextBlob


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sentiment():
    # Download the web page using requests

    url = request.form['url']
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    print("the text of the blog is",text)
    
    article.nlp()

   
    summary = article.summary
    obj = TextBlob(summary)
    sentiment = obj.sentiment.polarity
    print(sentiment)
    
    return render_template('index.html', summary=summary, sentiment=sentiment)    

if __name__ == '__main__':
    app.run(debug=True)