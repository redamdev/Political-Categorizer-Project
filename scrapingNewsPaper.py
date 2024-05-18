import requests 
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords


# Have a copy of the stop words
nltk.download('stopwords')
stopWords = set(stopwords.words('english'))


#start of the class and pass the url
def scrapingLink(url):

    try:
        #send the requests to scrape the article
        response = requests.get(url)

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
            title = 'no title found'

        
        #Extract the date
        dateTag = soup.find('meta', attrs={'property': 'article:published'})
        if dateTag:
            date = dateTag['content'].strip()
        else:
            date = 'no Date'
        

        #Extract the publisher
        publisherTag = soup.find('meta', attrs={'name': 'publisher'})
        if publisherTag and 'content' in publisherTag.attrs:
            publisher = publisherTag['content'].strip()
        else:
            publisher = 'no Publisher name found in the aticle'
            
            

        #Extract the body
        bodyTag = soup.find_all('p')
        body = body = ' '.join([p.get_text().strip() for p in bodyTag])

        # Remove stop words from the body of the article
        bodyWords = body.split()
        filteredBody = [word for word in bodyWords if word.lower() not in stopWords]
        body = ' '.join(filteredBody)

        return title, date, publisher, body


    except Exception as err:
        print(f"Error occured")
        return 'no title' , 'no date' , 'no publisher' , 'no body'
        
    
 

if __name__ == "__main__":
    url = 'https://www.foxnews.com/us/maryland-woman-pleads-guilty-conspiracy-alleged-extremist-plot-attack-baltimore-power-grid'
    title, date, publisher, body = scrapingLink(url)

    if title:
        print("Title:", title)
        print("Publisher:", publisher)
        print("Date Published:", date)
        print("Body:", body)
    else:
        print("Failed to extract article information.")
