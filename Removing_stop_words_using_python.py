# Create Beautiful soup obejct in Python and perform Parsing
from bs4 import BeautifulSoup
import urllib.request
page= urllib.request.urlopen('https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=newjersey')
soup=BeautifulSoup(page,'html.parser')
print(soup)

# Perform word count frequency

import nltk
from nltk.tokenize import word_tokenize
text=soup.get_text(strip=True)
word_tokens=word_tokenize(text)
cts=nltk.FreqDist(word_tokens)
cts.plot(20)

# Remove Special Characters 

import re
text2= re.sub("[^A-Za-z]+"," ",text)
print(text2)
import nltk
from nltk.tokenize import word_tokenize
word_tokens=word_tokenize(text2)
print(word_tokens)
cts=nltk.FreqDist(word_tokens)
cts.plot(20)

# Import Stop words

from nltk.corpus import stopwords
filtered_list=[]
stop_words = set(stopwords.words('english'))
stop_words

# Match stop word lists and  word tokens 

for word in word_tokens:
    if word not in stop_words:
        filtered_list.append(word)

filtered_list






