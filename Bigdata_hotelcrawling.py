import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_score(html_list, get_list, j):
    label = html_list[j].attrs["alt"]
    get_list.append(label[8:])
    return get_list

def get_reviewcount(html_list, get_list, j):
    text = html_list[j].get_text()
    text = text.replace("\n", "").strip()
    get_list.append(text[:-5])
    return get_list

def get_price(html_list, get_list, j):
     # 가격
    text = html_list[j].get_text()
    text = text.replace("\n", "").strip()
    get_list.append(text)
    return get_list

hotel_name = list()
score_list = list()
number_of_review = list()
price_list = list()

for i in range(0, 372, 30):
    print(i)
    url = "https://www.tripadvisor.co.kr/Hotels-g983296-oa" + str(i) + "-Jeju_Island-Hotels.html"
    time.sleep(15)
    html = requests.get(url) ##requests 를 이용해서 url의 html 파일을 가져옴
    soup = BeautifulSoup(html.text, "html.parser") ##가져온 html 파일을 html parser를 통해서 정리
    html_hotel_list = soup.findAll("div", {"class":"listing_title"})
    # <span class="ui_merchandising_pill sponsored_v2">스폰서</span>
    html_label_list = soup.findAll("a", {"data-clicksource": "BubbleRating"})
    html_reviewcount_list = soup.findAll("a", {"class": "review_count"})
    html_price_list = soup.findAll("div", {"data-sizegroup": "mini-meta-price"})

    j = 0
    # 호텔이름   
    for line in html_hotel_list:
        text = line.get_text()
        text = text.replace("\n", "").strip()
        if '스폰서' not in text:
            hotel_name.append(text)
            price_list = get_price(html_price_list, price_list, j)
            number_of_review = get_reviewcount(html_reviewcount_list, number_of_review, j)
            score_list = get_score(html_label_list, score_list, j)
        j += 1
    #time.sleep(5)    

print(len(hotel_name))
print(len(price_list))

multi_page_result = list()
for hotel, price, score, review_number in zip(hotel_name, price_list, score_list, number_of_review):
    row_data = [hotel, price, score, review_number]
    multi_page_result.append(row_data)


information_hotel = pd.DataFrame(multi_page_result, columns =['hotel', 'price', 'score', 'review_number'])

# information_hotel
information_hotel.to_csv('hotel_review.csv')