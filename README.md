# Overview of Project Functionality
The website is deployed using Vercel at this link for now: https://researchify-phi.vercel.app/.
***Researchify*** is a website that gathers research papers by category from **ARXIV**, obtaining each paper's abstract, title, link, and other relevant information. It returns a random selection of five recent articles from the categories of mathematics, statistics, computer science, quantitative finance, and electrical engineering and systems science. Then, it displays these articles to the user, with the ability to generate new random selections of articles. <!-- Users can also save their favorite articles if they have an account, and they can access these saved articles on the website. -->

# Technologies
I utilized ARXIV's API, and I formulated queries that obtained papers from the appropriate category and submission date. I processed the Atom XML outputs from these requests utilizing Python's **BeautifulSoup** and **Requests** Library. In this process, I inspected ARXIV's API output to obtain the appropriate information, and I returned article information in the form of an Article object to encapsulate information.

I utilized the **Flask** Python framework as a backend server to render the results of the web-scraping and enable routing, utilizing **HTML** and **CSS** as my front-end, onto a webpage. I also utilized Python's **MathJax** LATEX display engine to appropriately display mathematical and scientific symbols. <!-- I will add authorization functionality, which enables users to store their favorite articles. These articles for each user will be stored on a **SQLite** database. I will also implement Docker and Kubernetes to increase scalability. I may add language translation functionality. -->

# Dependencies
To install all dependencies used by this project after cloning this project, from the base directory, run:
```
pip install -r requirements.txt
```
