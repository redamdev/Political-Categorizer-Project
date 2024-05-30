import newspaper
from newspaper import Article
import nltk
from nltk.corpus import stopwords
import ssl



# Disable SSL certificate verification
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Ensure stopwords are downloaded
nltk.download('stopwords', quiet=True)

# Load stopwords
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
    if len(article.text.split()) < 100:  
        print("video articles are not acceptable.")
        return False
    
    if article.meta_lang != 'en':
        print("Article not in English! Please provide an English article.")
        return False

    article_header = article.url.lower() + ' ' + ' '.join(article.meta_keywords or [])
    if not any(keyword in article_header for keyword in newsAndPolitics_keywords):
        print("Article is not in a valid category! Please provide an article in a valid category.")
        return False

    return True

def scrapingLink(url):
    try:
        if not url.startswith(('http://', 'https://')):
            print(f"Invalid URL Type! Provided URL: {url}")
            return None, None, None, None
        
        article = Article(url)
        article.download()
        article.parse()
        
        if not vailidateArticle(article):
            return None, None, None, None
        
        titleTag = article.title
        title = titleTag.strip() if titleTag else 'No title found'
        
        dateTag = article.publish_date
        date = dateTag.strftime('%Y-%m-%d') if dateTag else 'No publish date found in the article'
        
        publisher = article.source_url.strip() if article.source_url else 'Publisher not found.'
        
        body = article.text.strip()
        if body:
            bodyWords = body.split()
            filteredBody = [word for word in bodyWords if word.lower() not in stopWords]
            body = ' '.join(filteredBody)
        else:
            body = 'Body not found.'

        return title, date, publisher, body

    except newspaper.article.ArticleException:
        print(f"Provided URL [{url}] not found.")
        return None, None, None, None
    
    except Exception as err:
        print(f"Error occurred: {err}")
        return 'No title', 'No date', 'No publisher', 'No body'
