# @author: Alexander Chapman, Douglas Hale
# Will take the data and use it to train the model and complete testing

# Import necessary libraries
#from scrapeSingleArticle import scrapeSingleArticle # Runs when debugging

#from Model.scrapeSingleArticle import scrapeSingleArticle # Runs when using web

import os
import certifi
from joblib import load
os.environ['SSL_CERT_FILE'] = certifi.where()



"""
    After a url link is received, the model and vectorizer are loaded and then used to predict the classifier of the article.

    Functions:
        @predictArticle(string)
            Loads the model and vectorizer before taking the string argument and scraping the news article before predicting it's classifier using the model.
"""


def predictArticle(article):
    """
        Takes the string argument and scrapes the news article before predicting it's classifier using the model.

        Parameters:
            @url :: string
                The url of the article wanted scraped.

    """

    # Makes sure a string is given as the argument
    if not isinstance(article, str):
        raise ValueError("The argument is not a string.")  

    # Loads the model and the vectorizer
    """ Use with Debugger """
    #model = load('NewsBuster v2/backend/Model/nb_model.joblib')
    #vectorizer = load('NewsBuster v2/backend/Model/vectorizer.joblib')

    """ Use with Web """
    #model = load('Model/nb_model.joblib')
    #vectorizer = load('Model/vectorizer.joblib')

    """ Use with Tester"""
    model = load('nb_model.joblib')
    vectorizer = load('vectorizer.joblib')

    # The cleaned article is transformed by the vectorizer and then given to the model so it can predict its classifier.
    articleTest = vectorizer.transform([article])
    predicted_label = model.predict(articleTest)[0]

    return predicted_label

"""
predictions = []
bodies = []
with open("NewsBuster v2/backend/Model/Articles/CleanedArticles/LeftManual/Miriam Adelson and Kyrie.txt", 'r', encoding='utf-8') as f:
    bodies.append(f.read())
    
with open("NewsBuster v2/backend/Model/Articles/CleanedArticles/LeftManual/GOP Senate Hopeful Royce White Seems a Little Mad at The Daily Beast’s Reporting.txt", 'r', encoding='utf-8') as f:
    bodies.append(f.read())    

with open("NewsBuster v2/backend/Model/Articles/CleanedArticles/RightManual/Who are the Anti-Israel Protestors.txt", 'r', encoding='utf-8') as f:
    bodies.append(f.read())

for body in bodies:
    predictions.append(predictArticle(body))

articleUrls = [
        "https://www.newsmax.com/politics/nevada-senate-gop/2024/06/12/id/1168415/",
        "https://www.foxbusiness.com/media/california-businesses-band-together-demand-real-answers-blue-states-high-costs",
        "https://www.cnn.com/2024/05/28/politics/trump-closing-arguments-trial-analysis/index.html",
        "https://www.cnn.com/2024/03/17/politics/dark-money-fga-ashcroft-invs/index.html",
        "https://www.foxnews.com/media/embattled-dolton-mayor-tiffany-henyard-accused-politically-targeting-towns-own-park-district"]

for url in articleUrls:
    body = scrapeSingleArticle(url)[3]
    predictions.append(predictArticle(body))

i = 1
for predict in predictions:
    print(f"{i}: {predict}")
    print()
    i += 1
"""

