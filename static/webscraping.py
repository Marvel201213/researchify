import requests
from bs4 import BeautifulSoup
import random

class Article:
    def __init__(self, category, title, link, abstract):
        self.category = category
        self.title = title
        self.link = link
        self.abstract = abstract
    
    def get_category(self):
        return self.category
    
    def get_title(self):
        return self.title
    
    def get_link(self):
        return self.link

    def get_abstract(self):
        return self.abstract
    def __repr__(self):
        return f"Article(category={self.category}, title={self.title}, link={self.link}, abstract={self.abstract})"
    def __str__(self):
        return f"Article Category: {self.category}\nArticle Title: {self.title}\nArticle Link: {self.link}\nArticle Abstract: {self.abstract}"
    def to_string_condensed(self):
        return f"Article Category: {self.category}\nArticle Title: {self.title}\nArticle Link: {self.link}"

def generate_arxiv_pages(fields):
    pages = {}
    ARXIV_BASE_URL = "https://arxiv.org/list/"
    for category, total_articles in fields.items():
        category_pages = []
        for skip in range(0, total_articles, 25):
            page = f"{ARXIV_BASE_URL}{category}/recent?skip={skip}&show=25"
            category_pages.append(page)
        pages[category] = category_pages
    return pages
def scrape():
    ARXIV_FIELDS = {
    "math": 200,
    "stat": 190,
    "cs": 200,
    "eess": 190,
    "q-fin": 75,
    }
    arxiv_pages = generate_arxiv_pages(ARXIV_FIELDS)
    total_pages = 0
    store_allcats = []
    for category, category_pages in arxiv_pages.items():
        storage = set()
        for page in category_pages:
            try:
                processed_page = requests.get(page)
                if processed_page.status_code != 200:
                    return (f"Failed to retrieve HTML content. Status code: {processed_page.status_code}")
            except Exception as e:
                return (category)
                return (f"An error occurred: {e}")
            html_content = processed_page.text
            soup = BeautifulSoup(html_content, 'html.parser')
            data = soup.find_all('a', attrs = {'title':'Abstract'})
            increment = 0
            for abstract in data:
                href = abstract.get('href')
                if href:
                    storage.add('https://arxiv.org'+href)
        store_allcats.append((storage, category))
    random_allcats = []
    for storage in store_allcats:
        my_choices = list(storage[0])
        random_elements = random.sample(my_choices, 5)
        random_allcats.append((random_elements, storage[1]))
    randarticle_abstract = []
    for random_elements in random_allcats:
        randarticle_compilation = []
        for article in random_elements[0]:
            try:
                processed_article = requests.get(article)
                if processed_article.status_code != 200:
                    return (f"Failed to retrieve HTML content. Status code: {processed_article.status_code}")
            except Exception as e:
                print(article)
                return (f"An error occurred: {e}")
            html_content = processed_article.text
            soup = BeautifulSoup(html_content, 'html.parser')
            data_abstract = soup.find_all('blockquote')
            data_title = soup.find_all('h1', attrs = {'class':'title mathjax'})
            abstract = ''.join(data_abstract[0].find_all(string = True, recursive = False)).strip()
            title = ''.join(data_title[0].find_all(string = True, recursive = False)).strip()
            try:
                art_obj = Article(random_elements[1], title, article, abstract)
            except Exception as e:
                return ("Article object construction invalid")
            randarticle_abstract.append(art_obj)
                
    return randarticle_abstract

""" randarticle_abstract = scrape()
for i in randarticle_abstract:
    print(i.to_string_condensed()) """