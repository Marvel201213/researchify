# Overview of Project Functionality
***Researchify*** is a website that scrapes research papers by category from **ARXIV**, obtaining each paper's abstract, title, and link. It returns a random selection of five recent articles from the categories of mathematics, statistics, computer science, quantitative finance, and electrical engineering and systems science. Then, it displays these articles to the user, with the ability to generate new random selections of articles with filtering by category. Users can also save their favorite articles if they have an account, and they can access these saved articles on the website.

# Technologies
I scraped ARXIV utilizing Python's **BeautifulSoup** and **Requests** Library, sending an HTTP Get request to the page and constructing a BeautifulSoup object with this HTML content. In this process, I inspected ARXIV's link formation and HTML classes to accesss the appropriate content, and I returned article information in the form of an Article object to encapsulate information.

I utilized the **Flask** Python framework as a backend server to render the results of the web-scraping, utilizing **HTML** and **CSS** as my front-end, onto a webpage. I will add authorization functionality, which enables users to store their favorite articles. These articles for each user will be stored on a **SQLite** database. 

# Dependencies
To install all dependencies used by this project after cloning this project, from the base directory, run:
```
pip install -r requirements.txt
```
