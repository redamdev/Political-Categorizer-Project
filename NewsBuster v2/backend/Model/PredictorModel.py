# @author: Alexander Chapman, Douglas Hale
# Will take the data and use it to train the model and complete testing

# Import necessary libraries
from Model.scrapeSingleArticle import scrapeSingleArticle
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

    # Loads the model and the vectorizer
    model = load('Model/nb_model.joblib')
    vectorizer = load('Model/vectorizer.joblib')

    # Scrapes the article and returns the body, which is then cleaned before being used by the vectorizer and model.
    #article = scrapeSingleArticle(url)[3]
    #print(article)

    # The cleaned article is transformed by the vectorizer and then given to the model so it can predict its classifier.
    articleTest = vectorizer.transform([article])
    predicted_label = model.predict(articleTest)[0]

    # For each classifier, the probability of it being that is returned.
    probabilities = model.predict_proba(articleTest)[0]


    # Prints results
    """ print(f"Predicted Label: {predicted_label}")
    print(f"Probabilities: {probabilities}")
    print()
    """

    return predicted_label

"""
articleUrls = [
        "https://www.foxbusiness.com/media/california-businesses-band-together-demand-real-answers-blue-states-high-costs",
        "https://www.cnn.com/2024/05/28/politics/trump-closing-arguments-trial-analysis/index.html"]

for url in articleUrls:
    predictArticle(url)
    """
