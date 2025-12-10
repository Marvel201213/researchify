import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

class Article:
    def __init__(self, category, title, link, date, abstract, authors):
        self.category = category
        self.title = title
        self.link = link
        self.date = date
        self.abstract = abstract
        self.authors = authors
    
    def get_category(self):
        return self.category
    
    def get_title(self):
        return self.title
    
    def get_link(self):
        return self.link
    
    def get_date(self):
        return self.date

    def get_abstract(self):
        return self.abstract
    
    def get_authors(self):
        return self.authors
    
    def __repr__(self):
        return f"Article(category={self.category}, title={self.title}, link={self.link}, date={self.date}, abstract={self.abstract}, authors={self.authors})"
   
    def __str__(self):
        return f"Article Category: {self.category}\nArticle Title: {self.title}\nArticle Link: {self.link}\nDate: {self.date}\nArticle Abstract: {self.abstract}\nAuthors: {self.authors}"
    
    def to_string_condensed(self):
        return f"Article Category: {self.category}\nArticle Title: {self.title}\nArticle Link: {self.link}\nDate: {self.date}\nAuthors: {self.authors}"
    
    def to_dict(self):
        return {
            "category": self.category,
            "title": self.title,
            "link": self.link,
            "date": self.date,
            "abstract": self.abstract,
            "authors": self.authors
        }

def generate_arxiv_pages(fields):
    pages = {}
    API_BASE_URL = f"http://export.arxiv.org/api/query?"
    date_range = "["+ str(int(datetime.today().strftime('%Y'))-1) + datetime.today().strftime('%m%d') + "0000+TO+" +datetime.today().strftime('%Y%m%d') +"2359]"
    for category, total_articles in fields.items():
        category_pages = []
        for start_index in range(0, total_articles, 25):
            search_query = f"search_query={category}+AND+submittedDate:{date_range}"
            pagination = f"start={start_index}&max_results=25"
            sorting = "&sortBy=submittedDate&sortOrder=descending"
            page = f"{API_BASE_URL}{search_query}&{pagination}{sorting}"
            category_pages.append(page) 
        pages[category] = category_pages
    return pages

def scrape():
    ARXIV_FIELDS = {
        "cat:math.AC+OR+cat:math.AG+OR+cat:math.AP+OR+cat:math.AT+OR+cat:math.CA+OR+cat:math.CO+OR+cat:math.CT+OR+cat:math.CV+OR+cat:math.DG+OR+cat:math.DS+OR+cat:math.FA+OR+cat:math.GM+OR+cat:math.GN+OR+cat:math.GR+OR+cat:math.GT+OR+cat:math.HO+OR+cat:math.IT+OR+cat:math.KT+OR+cat:math.LO+OR+cat:math.MG+OR+cat:math.MP+OR+cat:math.NA+OR+cat:math.NT+OR+cat:math.OA+OR+cat:math.OC+OR+cat:math.PR+OR+cat:math.QA+OR+cat:math.RA+OR+cat:math.RT+OR+cat:math.SG+OR+cat:math.SP+OR+cat:math.ST": 200,
        "cat:stat.AP+OR+cat:stat.CO+OR+cat:stat.ME+OR+cat:stat.ML+OR+cat:stat.OT+OR+cat:stat.TH": 190,
        "cat:cs.AI+OR+cat:cs.AR+OR+cat:cs.CC+OR+cat:cs.CE+OR+cat:cs.CG+OR+cat:cs.CL+OR+cat:cs.CR+OR+cat:cs.CV+OR+cat:cs.CY+OR+cat:cs.DB+OR+cat:cs.DC+OR+cat:cs.DL+OR+cat:cs.DM+OR+cat:cs.DS+OR+cat:cs.ET+OR+cat:cs.FL+OR+cat:cs.GL+OR+cat:cs.GR+OR+cat:cs.GT+OR+cat:cs.HC+OR+cat:cs.IR+OR+cat:cs.IT+OR+cat:cs.LG+OR+cat:cs.LO+OR+cat:cs.MA+OR+cat:cs.MM+OR+cat:cs.MS+OR+cat:cs.NA+OR+cat:cs.NE+OR+cat:cs.NI+OR+cat:cs.OH+OR+cat:cs.OS+OR+cat:cs.PF+OR+cat:cs.PL+OR+cat:cs.RO+OR+cat:cs.SC+OR+cat:cs.SD+OR+cat:cs.SE+OR+cat:cs.SI+OR+cat:cs.SY": 200,
        "cat:eess.AS+OR+cat:eess.IV+OR+cat:eess.SP+OR+cat:eess.SY": 190,
        "cat:q-fin.CP+OR+cat:q-fin.EC+OR+cat:q-fin.GN+OR+cat:q-fin.MF+OR+cat:q-fin.PM+OR+cat:q-fin.PR+OR+cat:q-fin.RM+OR+cat:q-fin.ST+OR+cat:q-fin.TR": 75,
    }       
    arxiv_pages = generate_arxiv_pages(ARXIV_FIELDS)
    total_pages = 0
    store_allcats = []
    for category, category_pages in arxiv_pages.items():
        storage = []
        for page in category_pages:
            try:
                processed_page = requests.get(page)
                if processed_page.status_code != 200:
                    return (f"Failed to retrieve XML content from API Request. Status code: {processed_page.status_code}")
            except Exception as e:
                return (category)
                return (f"An error occurred: {e}")
            xml_content = processed_page.text
            soup = BeautifulSoup(xml_content, 'lxml-xml')
            data = soup.find_all('entry')
            for entry in data:
                href = entry.find('id').text
                date = entry.find('updated').text
                abstract = entry.find('summary').text
                title = entry.find('title').text
                category = entry.find('arxiv:primary_category').attrs['term'] if entry.find('arxiv:primary_category') else "N/A"
                storedauthors = entry.find_all('author')
                authors = []
                for author in storedauthors:
                    authors.append(entry.find('name').text)
                try:
                    art_obj = Article(category, title, href, date, abstract, authors)
                except Exception as e:
                    return ("Article object construction invalid")
                storage.append(art_obj)
        store_allcats.append(storage)
    random_allcats = []
    for storage in store_allcats:
        my_choices = list(storage)
        if (len(my_choices) < 5):
            random_elements = my_choices
        else:
            random_elements = random.sample(my_choices, 5)
        random_allcats.append(random_elements)           
    return random_allcats



#Debugging Print Statements: Observe running script from full path directory to Python Interpreter required for debugging
""" abstract = ''.join(data_abstract[0].find_all(string = True, recursive = False)).strip()
title = ''.join(data_title[0].find_all(string = True, recursive = False)).strip() """
""" randarticle_abstract = scrape()
for i in randarticle_abstract:
    for obj in i:
        print(obj.to_string_condensed())  """

""" ARXIV_FIELDS = {
    "cat:math.AC+OR+cat:math.AG+OR+cat:math.AP+OR+cat:math.AT+OR+cat:math.CA+OR+cat:math.CO+OR+cat:math.CT+OR+cat:math.CV+OR+cat:math.DG+OR+cat:math.DS+OR+cat:math.FA+OR+cat:math.GM+OR+cat:math.GN+OR+cat:math.GR+OR+cat:math.GT+OR+cat:math.HO+OR+cat:math.IT+OR+cat:math.KT+OR+cat:math.LO+OR+cat:math.MG+OR+cat:math.MP+OR+cat:math.NA+OR+cat:math.NT+OR+cat:math.OA+OR+cat:math.OC+OR+cat:math.PR+OR+cat:math.QA+OR+cat:math.RA+OR+cat:math.RT+OR+cat:math.SG+OR+cat:math.SP+OR+cat:math.ST": 200,
    "cat:stat.AP+OR+cat:stat.CO+OR+cat:stat.ME+OR+cat:stat.ML+OR+cat:stat.OT+OR+cat:stat.TH": 190,
    "cat:cs.AI+OR+cat:cs.AR+OR+cat:cs.CC+OR+cat:cs.CE+OR+cat:cs.CG+OR+cat:cs.CL+OR+cat:cs.CR+OR+cat:cs.CV+OR+cat:cs.CY+OR+cat:cs.DB+OR+cat:cs.DC+OR+cat:cs.DL+OR+cat:cs.DM+OR+cat:cs.DS+OR+cat:cs.ET+OR+cat:cs.FL+OR+cat:cs.GL+OR+cat:cs.GR+OR+cat:cs.GT+OR+cat:cs.HC+OR+cat:cs.IR+OR+cat:cs.IT+OR+cat:cs.LG+OR+cat:cs.LO+OR+cat:cs.MA+OR+cat:cs.MM+OR+cat:cs.MS+OR+cat:cs.NA+OR+cat:cs.NE+OR+cat:cs.NI+OR+cat:cs.OH+OR+cat:cs.OS+OR+cat:cs.PF+OR+cat:cs.PL+OR+cat:cs.RO+OR+cat:cs.SC+OR+cat:cs.SD+OR+cat:cs.SE+OR+cat:cs.SI+OR+cat:cs.SY": 200,
    "cat:eess.AS+OR+cat:eess.IV+OR+cat:eess.SP+OR+cat:eess.SY": 190,
    "cat:q-fin.CP+OR+cat:q-fin.EC+OR+cat:q-fin.GN+OR+cat:q-fin.MF+OR+cat:q-fin.PM+OR+cat:q-fin.PR+OR+cat:q-fin.RM+OR+cat:q-fin.ST+OR+cat:q-fin.TR": 75,
}
print(generate_arxiv_pages(ARXIV_FIELDS)) """