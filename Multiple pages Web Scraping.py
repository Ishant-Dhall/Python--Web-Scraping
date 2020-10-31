
from bs4 import BeautifulSoup
import math
import pandas as pd
import json
import requests
import time
reviews=[]
url = 'https://www.productreview.com.au/listings/bingle' # Providing the URL of the web page
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
for pg in range(1,10): # Number of pages to be selected (1,n)
    pg = url + '?page=' + str(pg) +'#reviews'    # Pattern of the web page to loop over several pages
    page=requests.get(pg)
    soup = BeautifulSoup(page.text, "html.parser")
    time.sleep(2)
    for reviewBox in soup.findAll("div", {"itemprop": "review"}):
       
                review_title = reviewBox.find('h3', {"class": "mb-2_3ol"}).text    # Associated HTML tags 
                review_text = reviewBox.find('p', {"class": "mb-0_2CX"}).text
                review_date = reviewBox.find('meta', {'itemprop': 'datePublished'})['content']
                review_stars = reviewBox.find('meta', {'itemprop': 'ratingValue'})['content']
                reviews.append([review_title, review_text, review_date, review_stars])

Bingle = pd.DataFrame(reviews,columns=['title', 'review', 'date', 'stars'])
print(Bingle) # 2.0
