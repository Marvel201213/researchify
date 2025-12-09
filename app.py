from flask import Flask, render_template
from static import webscraping

app = Flask(__name__)
@app.route('/')
def rendered():
    articles = webscraping.scrape()
    return render_template('index.html', articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
