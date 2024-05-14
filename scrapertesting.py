import requests
from bs4 import BeautifulSoup
import re
from newspaper import Article

"""
response = requests.get("https://www.foxnews.com/us/maryland-woman-pleads-guilty-conspiracy-alleged-extremist-plot-attack-baltimore-power-grid")
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')
"""

article = Article("https://www.foxnews.com/us/maryland-woman-pleads-guilty-conspiracy-alleged-extremist-plot-attack-baltimore-power-grid")
article.download()
article.parse()
text = article.text

text = text.split(" ")  # Remove leading/trailing whitespace


text = [re.sub(r'\s+', ' ', word) for word in text] # Replace multiple spaces with a single space
text = [re.sub(r'[^\w\s+]', '', word) for word in text]  # Remove punctuation and special characters
text = [word.lower() for word in text] # Convert to lowercase 

print(text)
