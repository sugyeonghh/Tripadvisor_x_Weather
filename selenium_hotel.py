import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver

# 평점
def get_score(html_list, get_list, j):
    label = html_list[j].attrs["alt"]
    get_list.append(label[8:])
    return get_list

# 리뷰 몇 개인지
def get_reviewcount(html_list, get_list, j):
    text = html_list[j].get_text()
    text = text.replace("\n", "").strip()
    get_list.append(text[:-5])
    return get_list

# 갸격
def get_price(html_list, get_list, j):
    text = html_list[j].get_text()
    text = text.replace("\n", "").strip()
    get_list.append(text)
    return get_list

hotel_name = list()
score_list = list()
number_of_review = list()
price_list = list()
location_list = list()

# chrome driver 
driver = webdriver.Chrome('C:\\Users\\sec-1\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')

url = 'https://www.tripadvisor.co.kr/Hotels-g983296-oa30-Jeju_Island-Hotels.html'
driver.get(url)
time.sleep(10)

# parser 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

html_hotel_list = soup.findAll("div", {"class":"listing_title"})
html_label_list = soup.findAll("a", {"data-clicksource": "BubbleRating"})
html_reviewcount_list = soup.findAll("a", {"class": "review_count"})
html_price_list = soup.findAll("div", {"data-sizegroup": "mini-meta-price"})

j = 0

"""def get_location(get_list, j):
    driver.find_element_by_xpath('//*[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]').click()
    #driver.find_element_by_class_name('review_count').click()
    # driver.find_element_by_xpath('//*[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div[1]').click()
    time.sleep(10)
    # 새로 열린 탭으로 활성 탭 변경
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(10)

    # parser 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    #<span class="public-business-listing-ContactInfo__ui_link--1_7Zp public-business-listing-ContactInfo__level_4--3JgmI">서귀포 안덕면 신화역사로304번길 38</span>
    html_location_list = soup.findAll("span", {"class" : "public-business-listing-ContactInfo__ui_link--1_7Zp public-business-listing-ContactInfo__level_4--3JgmI"})

    text = html_location_list[0].get_text()
    text = text.replace("\n", "").strip()
    get_list.append(text)
    print(get_list)
    driver.close()

    # 맨 처음 탭으로 변경
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)

    return get_list"""

# 호텔이름   
for line in html_hotel_list:
    text = line.get_text()
    text = text.replace("\n", "").strip()

    if '스폰서' not in text:
        hotel_name.append(text)
        price_list = get_price(html_price_list, price_list, j)
        number_of_review = get_reviewcount(html_reviewcount_list, number_of_review, j)
        score_list = get_score(html_label_list, score_list, j)

        # location
        if not driver.find_elements_by_class_name("adInner gptAd delayAd loaded"):
            driver.find_element_by_xpath('//*[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]/div[%s]/div/div[1]/div[2]/div[2]/div[2]/div[1]' %str(j+2)).click()
            #time.sleep(10)
            # 새로 열린 탭으로 활성 탭 변경
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(10)

            # parser 
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            #<span class="public-business-listing-ContactInfo__ui_link--1_7Zp public-business-listing-ContactInfo__level_4--3JgmI">서귀포 안덕면 신화역사로304번길 38</span>

            html_location_list = soup.findAll("span", {"class" : "public-business-listing-ContactInfo__ui_link--1_7Zp public-business-listing-ContactInfo__level_4--3JgmI"})

            text = html_location_list[0].get_text()
            text = text.replace("\n", "").strip()
            location_list.append(text)
            print(location_list)
            driver.close()

            # 맨 처음 탭으로 변경
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(10)
    j += 1
#time.sleep(5)

# 맨 처음 탭으로 변경
#driver.switch_to.window(driver.window_handles[0])
#time.sleep(10)

driver.close()

print(len(hotel_name))
print(len(price_list))

multi_page_result = list()
for hotel, price, score, review_number in zip(hotel_name, price_list, score_list, number_of_review):
    row_data = [hotel, price, score, review_number]
    multi_page_result.append(row_data)


information_hotel = pd.DataFrame(multi_page_result, columns =['hotel', 'price', 'score', 'review_number'])

# information_hotel
information_hotel.to_csv('hotel_review.csv')














# 날짜 
# 체험 날짜: 2019년 4월 -> 0-6/ 7~
"""date_list = []
html_date_list = soup.findAll("span",{"class":"location-review-review-list-parts-EventDate__event_date--1epHa"})
for line in html_date_list:
    text = line.get_text()
    date_list.append(text[7:])

print('len of date_list: ',len(date_list))
for i in date_list:
    print(i)

# 여행 유형
# 여행 유형: 나 혼자 여행함 -> 0-6/ 7~
trip_type_list = [] 
html_trip_type_list = soup.findAll("span",{"class":"location-review-review-list-parts-TripType__trip_type--3w17i"})
if html_trip_type_list: 
    for line in html_trip_type_list:
        text = line.get_text()
        trip_type_list.append(text[7:])

print('len of trip_type_list: ',len(trip_type_list))
for i in trip_type_list:
    print(i)"""