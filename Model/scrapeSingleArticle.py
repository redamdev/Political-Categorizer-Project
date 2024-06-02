# @authors: Harshitha M, Nermeen R
# Used for our backend ML training purposes
# Scrapes single articles so the text can be used

# Import necessary libraries
import newspaper
import nltk
from newspaper import Article
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import os
import certifi


os.environ['SSL_CERT_FILE'] = certifi.where()


# Global list of valid categories
VALID_CATEGORIES = [
    'politics', 'news', 'election', 'government', 'policy', 'congress', 'senate', 'house of representatives', 'legislation', "business"
] # refined search

VALID_CATEGORIES2 = [
    'abdication', 'absolute monarchy', 'allegiance', 'anarchism', 'annexation', 'aristocracy', 'autonomy',
    'balance of power', 'bicameral system', 'bipartisan government', 'bureaucracy',
    'campaign, political', 'civil liberty', 'civil service', 'colonization', 'communism', 'conservatism', 'constitution',
    'convention', 'corrupt practices', 'democracy', 'deportation', 'despotism', 'election', 'embargo', 'executive',
    'fascism', 'federal government', 'federation', 'geopolitics', 'gerrymander', 'government', 'impeachment',
    'imperialism', 'judiciary', 'legislature', 'lobbying', 'military government', 'nationalism', 'natural rights', 'parliamentary law',
    'political', 'political action committee', 'political science', 'populism', 'president', 'vice president', 
    'republic', 'republicanism', 'republican government', 'separation of powers', 'socialism', 'sovereignty','veto', 'voting'
] # extended search retreieved from https://www.infoplease.com/encyclopedia/social-science/government/concepts

# Creates a set of stop words (generic words)
nltk.download('stopwords')
stopWords = set(stopwords.words('english'))

def cleanBody(articleBody):
    bodyWords = articleBody.split()
    filteredBody = [word for word in bodyWords if word.lower() not in stopWords]
    articleBody = ' '.join(filteredBody)
    return articleBody

# A helper function that validates the given article
def vailidateArticle(article):
    
    # Validation #2: Check if the article is not a video article by checking the text size since video articles have more text
    if (len(article.text.split()) < 100):  
        print("video articles are not acceptable.")
        return False

    # Validation #3: Check if the article is in English
    if article.meta_lang != 'en':
        print("Article not in English! Please provide an English article.")
        return False

    # Validation #4: Check if the article category is valid
    # Retrieves the article url header, then performs text cleaning
    """
    article_header = article.url.lower() + ' ' + ' '.join(article.meta_keywords or [])
    if not any(keyword in article_header for keyword in VALID_CATEGORIES):
        print("Article is not in a valid category! Please provide a relevant article.")
        return False
        """

    # Final return statement to indicate that the article is valid
    return True


# Function that scrapes a single article using newspaper3k library
def scrapeSingleArticle(websiteUrl):
    # Exception Handling to catch errors
    try:        
        # Validation #1: Checks if the URL is valid (no other formats)
        if not websiteUrl.startswith(('http://', 'https://')):
            print(f"Invalid URL Type! Please provide a valid URL.")
            return 

        # Creates an article object of the website
        article = Article(websiteUrl)

        # Downloads & parses the article
        article.download()
        article.parse()

        # Validate article using the helper function
        if not vailidateArticle(article):
            return 

        # Extracts title, then performs text cleaning
        titleTag = article.title
        if titleTag:
            title = titleTag.strip()
        else:
           title = 'Title not found.'
        
        # Extracts the date published, then performs text cleaning
        dateTag = article.publish_date
        if dateTag:
            date = dateTag.strftime('%Y-%m-%d')
        else:
            date = 'Date not found.'

        # Extracts publisher, then performs text cleaning
        publisher = article.source_url.strip()
        if publisher:
            publisher = publisher
        else:
            publisher = 'Publisher not found.'
            
        # Extracts body of the article
        body = article.text.strip()
        if body:
            body = body
        else:
            body = 'Body not found.'


        # Removes stop words from the body of the article
        body = cleanBody(body)

        return title, date, publisher, body

    # Exception Case 1: Unable to retrieve article
    except newspaper.article.ArticleException:
        print(f"Provided URL [{websiteUrl}] not found.")
        return

    # Exception Case 2: All other errors
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return 
