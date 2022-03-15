# Import NLTK and bs4
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import requests
# Website URL
URL = "https://www.javatpoint.com/data-mining-world-wide-web"
# Page content from Website URL
website = requests.get(URL)
# parse html content
soup = BeautifulSoup(website.content, 'html.parser')
paras = soup.find_all("p")
for para in paras:
    text = para.get_text()
    word_tokens = word_tokenize(text)
    print(word_tokens)
