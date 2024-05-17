import requests
import string
import re
import newspaper
import pandas as pd
import mysql.connector
from bs4 import BeautifulSoup
from newspaper import Article
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline


# Connects to the mySQL database.
mydb = mysql.connector.connect(
    host="localhost",              
    user="root",          
    password="myPassword",        
    database="articles"   
)

cursor = mydb.cursor() # Allows us to execute SQL queries


###################################
#                                 #
#  This entire following section  # 
#  is an example of how we can    #
#  scrape a ton of articles from  #
#  classically biased sources     #
#                                 #
###################################

"""
# Grabs a section of the website to scrape from
source = newspaper.build('https://www.bbc.com/news')  

# Iterates over articles in section
for article in source.articles:
    print(article.url) # Just to see what we are collecting
    article.download()  # Download the article content
    article.parse()      # Parse the article (extract text or whatever we would need)

    # Store the article text so we can work on it
    text = article.text

    # Removes punctuation
    text = text.translate(str.maketrans('', '', string.punctuation)) 

    classification = "middle" # Sets the classification of the article

    # Insert the article with the classification into the database
    sql = "INSERT INTO articles (text, classification) VALUES (%s, %s)"
    values = (text, classification)

    cursor.execute(sql, values) # Executes the command
    mydb.commit() # Commits the changes to the database
"""



# Grabs everything in the table
query = "SELECT * FROM articles"  
cursor.execute(query)
results = cursor.fetchall()

id, X_train, y_train = zip(*results) # Splits the columns and assigns the data to training data

model = make_pipeline(
    CountVectorizer(),  # Convert text to bag-of-words vectors by splitting words and making everything lowercase
    MultinomialNB()     # Apply Naive Bayes algorithm
)
model.fit(X_train, y_train) # Is training the model with the text and classifications

