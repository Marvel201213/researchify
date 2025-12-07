from flask import Flask, render_template
from static import webscraping

app = Flask(__name__)
@app.route('/main')
def hello(articles = webscraping.scrape()):
    return render_template('index.html', articles=articles)
