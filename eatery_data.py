import pandas as pd
import requests
from bs4 import BeautifulSoup

result_list = list()

url = "https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d12453925-Reviews-Gozip_Dol_Wooluck_Jungmun-Seogwipo_Jeju_Island.html"

headers = {'User-Agent': 'Mozilla/5.0'}

html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, "html.parser")

review_list = list()
html_review_list = soup.findAll("div", attrs={"class": "prw_rup prw_reviews_stay_date_hsx"})

# print(html_review_list)
print("#######")

for line in html_review_list:
    text = line.get_text()
    review_list.append(text)

print(review_list)
