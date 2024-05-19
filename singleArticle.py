#@author Rizk, Maddi
import newspaper
from newspaper import Article
import re
import nltk
from nltk.corpus import stopwords


# Have a copy of the stop words
nltk.download('stopwords')
stopWords = set(stopwords.words('english'))

newsAndPolitics_keywords = [
    'politics', 'news', 'election', 'government', 'policy', 'congress', 'senate', 'house of representatives', 'legislation',
    'abdication', 'absolute monarchy', 'allegiance', 'anarchism', 'annexation', 'aristocracy', 'autonomy',
    'balance of power', 'bicameral system', 'bipartisan government', 'bureaucracy',
    'campaign, political', 'civil liberty', 'civil service', 'colonization', 'communism', 'conservatism', 'constitution',
    'convention', 'corrupt practices', 'democracy', 'deportation', 'despotism', 'election', 'embargo', 'executive',
    'fascism', 'federal government', 'federation', 'geopolitics', 'gerrymander', 'government', 'impeachment',
    'imperialism', 'judiciary', 'legislature', 'lobbying', 'military government', 'nationalism', 'natural rights', 'parliamentary law',
    'political', 'political action committee', 'political science', 'populism', 'president', 'vice president', 
    'republic', 'republicanism', 'republican government', 'separation of powers', 'socialism', 'sovereignty','veto', 'voting'
]

# A helper function that validates the given article
def vailidateArticle(article):
    
    # Validation #2: Check if the article is not a video article by checking the text size since video articles have more text
    if len(article.text.split()) < 100:  
        print("video articles are not acceptable.")
        return False
    
    # Validation #3: Check if the article is in English
    if article.meta_lang != 'en':
        print("Article not in English! Please provide an English article.")
        return False

    # Validation #4: Check if the article category is valid
    # Retrieves the article url header, then performs text cleaning
    article_header = article.url.lower() + ' ' + ' '.join(article.meta_keywords or [])
    if not any(keyword in article_header for keyword in newsAndPolitics_keywords):
        print("Article is not in a valid category! Please provide an article in a valid category.")
        return False

    return True


#start of the class and pass the url
def scrapingLink(url):

    try:
        # Validation #1: Checks if the URL is valid (no other formats)
        if not url.startswith(('http://', 'https://')):
            print(f"Invalid URL Type! Provided URL: {url}")
            return None, None, None, None
        
        
        # Creates an article object of the website
        article = Article(url)
        article.download()
        article.parse()
         
        #validate the article to be in the news/political categeory
        if not vailidateArticle(article):
            return None, None, None, None
        
        
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
           date = 'no Pulish_Date is found in the article'
           
        
        #Extract the publisher
        publisher = article.source_url.strip()
        if publisher:
            publisher = publisher
        else:
            publisher = 'Publisher not found.'
            
            
        #Extract the body
        body = article.text.strip()
        if body:
            body = body
        else:
            body = 'Body not found.'

        # Remove stop words from the body of the article
        bodyWords = body.split()
        filteredBody = [word for word in bodyWords if word.lower() not in stopWords]
        body = ' '.join(filteredBody)

        return title, date, publisher, body


    except newspaper.article.ArticleException:
        print(f"Provided URL [{url}] not found.")
        return None, None, None, None
    
    except Exception as err:
        print(f"Error occured")
        return 'no title' , 'no date' , 'no publisher' , 'no body'
        
        
                ###############################################################################
                ###############################################################################
                ############################ End Of File ######################################
                ###############################################################################
                ###############################################################################
