# @author: Alexander Chapman, Douglas Hale
# Will take the data and use it to train the model and complete testing

# Import necessary libraries
from scrapeSingleArticle import scrapeSingleArticle
from collectTrainingData import CollectTrainingData

import os
import certifi
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from joblib import dump, load
os.environ['SSL_CERT_FILE'] = certifi.where()


""" Every time a user enters an input a model will be loaded and a question asked"""
class NBModel:
    """
        A Naive Bayes model where it can be created from scratch with given data or loaded into a saved model.
    
        Class Variables:
            @vectorizer :: CountVectorizer Object
                Used to transform data into vectors of 2 and 3 word phrases and phrase counts, which will be used by the model when training and testing.
            @model :: MultinomialNB Object
                Will be trained using a multinomial naive bayes algorithm and used to make predictions.
        
        Instance Variables:
            @x_test :: string()
                A tuple of the articles taken from the initial dataset and chosen for testing.
            @y_test :: string()
                A tuple of the classifiers taken from the initial dataset and chosen for testing.

        Methods:
            @__init__()
                Constructor that will declare and initialize the instance variables, @x_test and @y_test, to empty tuples.

            @trainModel(string, string(), string())
                Will use a given directory path with news sources and classifiers to collect the data and then split it into training and testing.

            @predictArticle(string)
                Takes the string argument and scrapes the news article before predicting it's classifier using the model.

            @testTrainingAccuracy()
                Uses the instance variables x_test and y_test to test model accuracy while also reporting its Confusion Matrix and Classification Report.

            @loadModel(string)
                Takes a file path as the argument and uses it to load that model into the current session.
    """

    # Class Variables
    vectorizer = CountVectorizer(ngram_range=(2,3))
    model = MultinomialNB()

    
    def __init__(self):
        """
            Constructor that will declare and initialize the instance variables, @x_test and @y_test, to empty tuples.

            Instance Variables:
                @x_test :: string()
                    A tuple of the articles taken from the initial dataset and chosen for testing.
                @y_test :: string()
                    A tuple of the classifiers taken from the initial dataset and chosen for testing.
        """

        self.x_test = () 
        self.y_test = ()


    
    def trainModel(self, trainingData):
        """
            Creates and train a new multinomial naive bayes model with news articles by given sources and their given classifiers. The path to the articles is then used to collect training data from every source.

            Parameters:
                @directory_path :: string
                    The path to the directory that contains the source folders of docx files. 
                @sources :: string()
                    Tuple that contains the names of the news sources. This should be in the same order as the folder. 
                @classifiers :: string()
                    Tuple that contains the classifications of the sources. They should correspond to source at same index in sources.
        """
        

        # Collects the data and returns it in a 2D list with [article body, classifier] being the inside form.
        #trainingData = CollectTrainingData()(directory_path, sources, classifiers)
        x, y = trainingData

        # Seperates data into being for training or test with 80% of articles being used for training.
        x_train, self.x_test, y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # Transform training articles into vector form and have the vectorizer remember these by adding 'fit'.
        vectorized_x_train = self.vectorizer.fit_transform(x_train)

        # Trains the model with the given articles and classifiers, then saves and returns it.
        self.model.fit(vectorized_x_train, y_train)
        dump(self.model, 'Model/nb_model.joblib')
        dump(self.vectorizer, 'Model/vectorizer.joblib')

    
    def predictArticle(self, url):
        """
            Takes the string argument and scrapes the news article before predicting it's classifier using the model.
 
            Parameters:
                @url :: string
                    The url of the article wanted scraped.
        
        """
        # Scrapes the article and returns the body, which is then cleaned before being used by the vectorizer and model.
        article = scrapeSingleArticle(url)[3]
        processed_article = CollectTrainingData()._cleanText(article)
        print(processed_article)

        # The cleaned article is transformed by the vectorizer and then given to the model so it can predict its classifier.
        articleTest = self.vectorizer.transform([processed_article])
        predicted_label = self.model.predict(articleTest)[0]

        # For each classifier, the probability of it being that is returned.
        probabilities = self.model.predict_proba(articleTest)[0]
       

        # Prints results
        print(f"Predicted Label: {predicted_label}")
        print(f"Probabilities: {probabilities}")
        print()



    def testTrainingAccuracy(self):
        """
            Uses the instance variables x_test and y_test to test model accuracy while also reporting its Confusion Matrix and Classification Report. 
        """

        # Vectorizes the x_test data for use by the model, before it is then used by the model to predict the classifiers.
        vectorized_x_test = self.vectorizer.transform(self.x_test)
        y_pred = self.model.predict(vectorized_x_test) 

        # Collects how accurate the model was by comparing the predicted classifiers against the actual ones. 
        accuracy = accuracy_score(self.y_test, y_pred)

        # Shows the exact numbers of predictions made for each classifier compared to actual results. 
        conf_matrix = confusion_matrix(self.y_test, y_pred) 

        # Can tell how precise the model was and how often it recalled the classes.
        class_report = classification_report(self.y_test, y_pred)

        # Prints results
        print(f"Model accuracy on test data: {accuracy:.2f}") 
        print("Confusion Matrix:\n", conf_matrix)
        print("Classification Report:\n", class_report)



    def load_model(self, model_path, vectorizer_path):
        """
            Takes a file path as the argument and uses it to load that model into the current session.
 
            Parameters:
                @file_path :: string
                    The path to the file that stores the model.

            Returns:
                @self.model :: MultibinomialNB Object
                    The model that has been loaded.
        
        """
        self.model = load(model_path)
        self.vectorizer = load(vectorizer_path)



def main():
    newsSources = ["AP", "CNN", "NBC", "Forbes", "Newsweek", "Daily_Caller"]
    classes = ["middle", "left", "left", "middle", "right", "right"]
    model = NBModel()
    #model.load_model('nb_model.joblib', 'vectorizer.joblib')
    trainingData = CollectTrainingData()._readyModelData("Model/Articles/CleanedArticles/", newsSources, classes)
    model.trainModel(trainingData)
    model.testTrainingAccuracy()

    articleUrls = [
        "https://www.foxbusiness.com/media/california-businesses-band-together-demand-real-answers-blue-states-high-costs",
        "https://www.cnn.com/2024/05/28/politics/trump-closing-arguments-trial-analysis/index.html"]

    for url in articleUrls:
        model.predictArticle(url)
    
main()

exit()
"""
for y in y_test:
    print("Test: " + y)

for y in y_train:
    print("Train: " + y)


for i in range(len(X_test)):
    if y_test[i] != y_pred[i]:
        print(X_test[i])
        print(y_test[i])
        print(y_pred[i])
        print()
"""


X_test = []
Y_test = []
i = 0
