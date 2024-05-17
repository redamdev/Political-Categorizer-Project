import requests
from bs4 import BeautifulSoup
import re
import newspaper
from newspaper import Article
from sklearn.feature_extraction.text import CountVectorizer
import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline


mydb = mysql.connector.connect(
    host="localhost",              # Use 'localhost' for your local machine
    user="root",            # Replace with your MySQL username
    password="Chappy98",        # Replace with your MySQL password
    database="articles"   # Replace with your database name
)

cursor = mydb.cursor()



"""
response = requests.get("https://www.foxnews.com/us/maryland-woman-pleads-guilty-conspiracy-alleged-extremist-plot-attack-baltimore-power-grid")
response.raise_for_status()

soup = BeautifulSoup(regsponse.content, 'html.parser')


source = newspaper.build('https://www.bbc.com/news')  # Replace with the URL of your target website

# 2. Iterate over articles
for article in source.articles:
    print(article.url)
    article.download()  # Download the article content
    article.parse()      # Parse the article (extract title, text, etc.)

    # Store the article data (e.g., in a list, database, or CSV file)
    text = article.text
    title = article.title

File_object = open(r"Links.txt", "Access_Mode")


article = Article("https://www.foxnews.com/us/maryland-woman-pleads-guilty-conspiracy-alleged-extremist-plot-attack-baltimore-power-grid")
article.download()
article.parse()
text = article.text
classification = "right"

sql = "INSERT INTO articles (text, classification) VALUES (%s, %s)"
values = (text, classification)

cursor.execute(sql, values)

# Commit the changes to the database
mydb.commit()

print(cursor.rowcount, "record inserted.")
"""

query = "SELECT * FROM articles"  # Replace with your table name

cursor.execute(query)

results = cursor.fetchall()

id, X_train, y_train = zip(*results)


model = make_pipeline(
    CountVectorizer(),  # Convert text to bag-of-words vectors
    MultinomialNB()     # Apply Naive Bayes algorithm
)
model.fit(X_train, y_train)

"""
text = text.split(" ")  # Remove leading/trailing whitespace


# Fix the text. Some is jumbled and it is taking links that are in the middle. Remove those

text = [re.sub(r'\s+', ' ', word) for word in text] # Remove newline
text = [re.sub(r'[^\w\s+]', '', word) for word in text]  # Remove punctuation and special characters
text = [word.lower() for word in text] # Convert to lowercase 
"""


