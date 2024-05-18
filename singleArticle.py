import newspaper
from newspaper import Article
import re
import nltk
from nltk.corpus import stopwords


# Have a copy of the stop words
nltk.download('stopwords')
stopWords = set(stopwords.words('english'))


#start of the class and pass the url
def scrapingLink(url):

    try:
        article = Article(url)
        article.download()
        article.parse()

        #Extract the title
        titleTag = article.title
        if titleTag:
            title = titleTag.strip()
        else:
           title = 'no title found'

        
        #Extract the date
        dateTag = article.publish_date
        if dateTag:
            date = dateTag.strftime('%Y-%m-%d')
        else:
            date = 'no Date'
        

        #Extract the publisher
        publisher = article.source_url.strip()
            
        #Extract the body
        body = article.text.strip()

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
