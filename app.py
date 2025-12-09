from flask import Flask, render_template
from static import webscraping

app = Flask(__name__)
app.secret_key = ""
@app.route('/')
def home():
    articles = webscraping.scrape()
    return render_template('index.html', articles=articles)

@app.route('/saved')
def saved():
    pass    

@app.route('/login')
def login():
    pass

@app.route('/callback')
def callback():
    pass

@app.route('/logout')
def logout():
    pass

if __name__ == "__main__":
    app.run(debug=True)
