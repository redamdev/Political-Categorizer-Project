#@author Nermeen Rizk
#@author Harshitha Maddi
import newspaper
from newspaper import Article
import re
import nltk
from nltk.corpus import stopwords
import unittest



# Have a copy of the stop words
nltk.download('stopwords')
stopWords = set(stopwords.words('english'))

VALID_CATEGORIES = [
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


"""
Description:
    A helper function that validates an article by checking if it meets certain criteria.


Parameters:
    article (Article): The article to be validated.


Returns:
    bool: True if the article is valid, False otherwise.


Raises:
    None


Specifications:
    1. The function performs the following validations:
        - If the article is not a video article by checking the text size since video articles have more text.
        - If the article is in English.
        - If the article category is valid.
    2. If any of the desired validations fail, an error message is printed and False is returned.
    3. If all validations pass, the function returns True; meaning, the article is validated successfully.
"""


def validateArticle(article):
    # Validation #2: Check if the article is not a video article by checking the text size since video articles have more text
    if (len(article.text.split()) < 100):  
        print("Video articles are not acceptable!")
        return False


    # Validation #3: Check if the article is in English
    if article.meta_lang != 'en':
        print("Article not in English! Please provide an English article.")
        return False


    # Validation #4: Check if the article category is valid
    # Retrieves the article url header, then performs text cleaning
    article_header = article.url.lower() + ' ' + ' '.join(article.meta_keywords or [])
    if not any(keyword in article_header for keyword in VALID_CATEGORIES):
        print("Article is not in a valid category! Please provide a relevant article.")
        return False




    # Final return statement to indicate that the article is valid
    return True








"""
Description:
    A function that scrapes a single article using the newspaper3k library.


Parameters:
    websiteUrl (str): The URL of the website to be scraped.


Returns:
    title (str): The title of the article that was scraped,
    date (str): The date of the article that was scraped,
    publisher (str): The publisher of the article that was scraped,
    body (str): The body of the article that was scraped.


Raises:
    None


Specifications:
    1. Performs an initial validation to check if the URL is valid (no other formats).
    2. Creates an article object of the website.
    3. Downloads & parses the article.
    4. Validates the article by calling the helper function.
    5. Extracts title, date, publisher, and body of the article.
    6. Performs text cleaning on the title, date, publisher, and body.
    7. Returns the title, date, publisher, and body of the article.
    8. If any of the desired retrievals are not found, the function returns None.
    9. If the function is unable to run for any reason, the respective exception is raised.
"""


def scrapeSingleArticle(websiteUrl):
    # Exception Handling to catch errors
    try:        
        
        # Creates an article object of the website
        article = Article(websiteUrl)


        # Downloads & parses the article
        article.download()
        article.parse()


        # Validate article using the helper function
        if not validateArticle(article):
            return None, None, None, None


        # Extracts title, then performs text cleaning
        title = article.title.strip() if article.title else 'Title not found.'
       
        # Extracts the date published, then performs text cleaning
        date = article.publish_date.strftime('%Y-%m-%d') if article.publish_date else 'Date not found.'


        # Extracts publisher, then performs text cleaning
        publisher = article.source_url.strip() if article.source_url.strip() else 'Publisher not found.'


        # Extracts body of the article
        body = article.text.strip() if article.text.strip() else 'Body not found.'


        # Removes stop words from the body of the article
        bodyWords = body.split()
        filteredBody = [word for word in bodyWords if word.lower() not in stopWords]
        body = ' '.join(filteredBody)


        return title, date, publisher, body


    # Exception Case 1: Unable to retrieve article
    except newspaper.article.ArticleException:
        print(f"Provided URL [{websiteUrl}] not found.")
        return None, None, None, None


    # Exception Case 2: All other errors
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return None, None, None, None





"""
Description:
    A class to test the scraper functions.
    The class contains separate tests for each scraper function.
    Uses the documentation from https://docs.python.org/3/library/unittest.html


Parameters:
    None


Returns:
    None


Specifications:
    1. Tests the validateArticle function.
    2. Tests the scrapeSingleArticle function.
"""

class TestAll(unittest.TestCase):
    # Tests validateArticle function
    def test_validArticle1(self):
        validArticle = Article('https://www.bbc.com/news/world-us-canada-68790777')
        validArticle.download()
        validArticle.parse()
        self.assertEqual( validateArticle(validArticle), True)


    def test_validArticle2(self):
        validArticle = Article('https://www.cnn.com/2024/05/23/politics/republicans-2024-election-analysis/index.html')
        validArticle.download()
        validArticle.parse()
        self.assertEqual(validateArticle(validArticle), True)
        
     
    def test_validArticle3(self):
        validArticle = Article('https://www.cnn.com/2024/05/29/politics/supreme-court-trump-what-matters/index.html')
        validArticle.download()
        validArticle.parse()
        self.assertEqual(validateArticle(validArticle), True)
        
     
    def test_validArticle4(self):
        validArticle = Article('https://www.cnn.com/politics/live-news/trump-hush-money-trial-05-29-24/index.html')
        validArticle.download()
        validArticle.parse()
        self.assertEqual(validateArticle(validArticle), True)
        
    #Test NonValid Article  
    #Sport not political category
    def test_InvalidArticle1(self):
        validArticle = Article('https://www.cnn.com/2024/05/28/health/alpacas-h5n1-bird-flu/index.html')
        validArticle.download()
        validArticle.parse()
        self.assertEqual(validateArticle(validArticle), False)
    
    #health category
    def test_InvalidArticle2(self):
        validArticle = Article('https://www.cnn.com/2024/05/13/health/ultraprocessed-food-bad-health-wellness/index.html')
        validArticle.download()
        validArticle.parse()
        self.assertEqual(validateArticle(validArticle), False)
        
    def test_InvalidArticle3(self):
        validArticle = Article('https://www.cnn.com/2024/05/29/entertainment/wolfs-trailer-george-clooney-brad-pitt/index.html')
        validArticle.download()
        validArticle.parse()
        self.assertFalse(validateArticle(validArticle))
    

    # not english article
    def test_nonEnglishArticle1(self):
        nonEnglishArticle = Article('https://elpais.com/ideas/2024-05-25/steven-levitsky-el-eje-ya-no-es-izquierda-derecha-sino-cosmopolitas-etnonacionalistas.html')
        nonEnglishArticle.download()
        nonEnglishArticle.parse()
        self.assertEqual(validateArticle(nonEnglishArticle), False)


    def test_nonEnglishArticle2(self):
        nonEnglishArticle = Article('https://www.lefigaro.fr/festival-de-cannes/cannes-2024-le-palmares-complet-de-la-77e-edition-du-festival-20240525')
        nonEnglishArticle.download()
        nonEnglishArticle.parse()
        self.assertEqual(validateArticle(nonEnglishArticle), False)
        
    
    def test_nonEnglishArticle3(self):
        nonEnglishArticle = Article('https://www.bbc.com/arabic/articles/cpw7z8lg8nwo')
        nonEnglishArticle.download()
        nonEnglishArticle.parse()
        self.assertFalse(validateArticle(nonEnglishArticle))
    
    def test_nonEnglishArticle4(self):
        nonEnglishArticle = Article('https://www.bbc.com/arabic/articles/cz44ee8qx05o')
        nonEnglishArticle.download()
        nonEnglishArticle.parse()
        self.assertFalse(validateArticle(nonEnglishArticle))  
    
        
    
   #test video articles
    def test_videoArticle1(self):
        videoArticle = Article('https://www.foxnews.com/video/6353692157112')
        videoArticle.download()
        videoArticle.parse()
        self.assertEqual(validateArticle(videoArticle), False)


    def test_videoArticle2(self):
        videoArticle = Article('https://www.cnn.com/videos')
        videoArticle.download()
        videoArticle.parse()
        self.assertEqual(validateArticle(videoArticle), False)
        
    def test_videoArticle3(self):
        videoArticle = Article('https://www.bbc.com/arabic/articles/c7251d497ygo')
        videoArticle.download()
        videoArticle.parse()
        self.assertFalse(validateArticle(videoArticle))
        
    def test_videoArticle4(self):
        videoArticle = Article('https://www.bbc.com/arabic/articles/czq5v2q6vl1o')
        videoArticle.download()
        videoArticle.parse()
        self.assertFalse(validateArticle(videoArticle))
        
        
   
    # Tests scrapeSingleArticle function
    def test_scrapeSingleArticle1(self):
        validUrl = 'https://www.nbcnews.com/politics/congress/key-senate-democrats-meeting-chief-justice-roberts-alito-ethics-rcna154052'    
        title, date, publisher, body = scrapeSingleArticle(validUrl)
        self.assertNotEqual(title, None)
        self.assertNotEqual(date, None)
        self.assertNotEqual(publisher, None)
        self.assertNotEqual(body, None)


    def test_scrapeSingleArticle2(self):
        validUrl = 'https://www.nbcnews.com/politics/congress/key-senate-democrats-meeting-chief-justice-roberts-alito-ethics-rcna154052'    
        title, date, publisher, body = scrapeSingleArticle(validUrl)
        self.assertNotEqual(title, None)
        self.assertNotEqual(date, None)
        self.assertNotEqual(publisher, None)
        self.assertNotEqual(body, None)
        
    def test_scrapeSingleArticle3(self):
        validUrl = 'https://www.cnn.com/politics/live-news/trump-hush-money-trial-05-29-24/index.html'    
        title, date, publisher, body = scrapeSingleArticle(validUrl)
        self.assertNotEqual(title, None)
        self.assertNotEqual(date, None)
        self.assertNotEqual(publisher, None)
        self.assertNotEqual(body, None)
        


# Calls the tester class to run the tests
if __name__ == '__main__':
    unittest.main()
