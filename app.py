from flask import Flask, render_template, jsonify
from static import webscraping

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', articles = [])

@app.route('/get-articles')
def get_articles():
    articles = webscraping.scrape()
    json_prepped_articles = []
    for category in articles:
        json_cat_prep = []
        for obj in category:
            json_cat_prep.append(obj.to_dict())
        json_prepped_articles.append(json_cat_prep)
    print(json_prepped_articles)
    return jsonify(articles= json_prepped_articles)
    
@app.route('/saved')
def saved():
    return render_template('saved.html')

if __name__ == "__main__":
    app.run(debug=True)
