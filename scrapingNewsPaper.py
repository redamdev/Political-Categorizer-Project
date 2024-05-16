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

        #Extract the title
        titleTag = soup.find('title')
        if titleTag:
            title = titleTag.string.strip()
        else:
            'no title found'

        
        #Extract the date
        dateTag = soup.find('meta', attrs={'property': 'article:published_time'})
        if dateTag:
            date = dateTag['content'].strip()
        else:
            'no Date'
        

        #Extract the publisher
        publisherTag = soup.find('meta', attrs={'name': 'publisher'})
        if publisherTag:
            publisher = publisherTag['content'].strip()
        else:
            'no Publisher name found in the aticle'
            

        #Extract the bode
        bodyTag = soup.find_all('p')
        body = body = ' '.join([p.get_text().strip() for p in bodyTag])



    except requests.exceptions.HTTPError as httpError:
        print(f"Error Occured in scraping the url")
    except Exception as err:
        print(f"Error occured")
