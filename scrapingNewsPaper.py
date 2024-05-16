import requests
from bs4 import BeautifulSoup
import re

#start of the class and pass the url
def scrapeNewsArticleLink(url):

    try:
        #send the requests to scarpe the article
        response = requests(url)

        #check the code of requests
        response.raise_for_status()

        #getting the content as a text
        text = response.text

        #parsing the content of the html
        soup = BeautifulSoup(response.content, 'html.parser')




    except requests.exceptions.HTTPError as httpError:
        print(f"Error Occured in scraping the url")
    except Exception as err:
        print(f"Error occured")