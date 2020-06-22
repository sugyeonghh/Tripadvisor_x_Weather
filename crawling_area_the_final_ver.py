from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import time
import datetime

# chrome driver 
driver = webdriver.Chrome('C:/Chrome_driver/chromedriver.exe')


place_list = [
    # 해변 
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d2487434-Reviews-or125-Yongmeori_Beach-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d550694-Reviews-or315-Hamdeok_Beach-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d4504781-Reviews-or305-Hyeopjae_Beach-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d10126654-Reviews-or110-Woljeongri_Beach-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d7049502-Reviews-or95-Jungmun_Saekdal_Beach-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d8667339-Reviews-or55-Geumneung_Eutteumwon_Beach-Jeju_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d9583049-Reviews-or45-Gimnyeong_Seonsegi_Beach-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d8790518-Reviews-or50-Gwangchigi_Beach-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d6352845-Reviews-or50-Sehwa_Beach-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d10586744-Reviews-or55-Iho_Tewoo_Beach-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d8790487-Reviews-or30-Pyoseon_Haevichi_Beach-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d9755433-Reviews-or25-Gwakji_Gwamul_Beach-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d19923114-Reviews-or0-Sogeum_Mak_Haebyeon-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d6876755-Reviews-or20-Samyang_Black_Sand_Beach-Jeju_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d16871842-Reviews-or0-Sanho_Beach-Jeju_Jeju_Island.html',

    # 산 
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d550726-Reviews-or355-Hallasan_National_Park-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d1582693-Reviews-or830-Seongsan_Ilchulbong-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d4223908-Reviews-or80-Songaksan_Mountain-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d6669874-Reviews-or60-Sanbangsan_Mountain-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d10464444-Reviews-or40-Saebyeol_Oreum-Jeju_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d8738109-Reviews-or15-Ttarabi_Oreum-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d18928117-Reviews-or0-Min_Oreum_Oradong-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d17325576-Reviews-or0-Gwetmul_Oleum-Jeju_Jeju_Island.html',
    
    # 공원
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d2204891-Reviews-or125-Spirited_Garden-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d2202426-Reviews-or230-Bijarim_Forest-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d2202425-Reviews-or90-Jeolmul_Natural_Forest_Resort-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d2204895-Reviews-or210-Hallim_Park-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d2204929-Reviews-or105-Jeju_Stone_Park-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d7287893-Reviews-or35-Jeju_April_3rd_Peace_Park-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d2204917-Reviews-or115-Yeomiji_Botanical_Garden-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d4094868-Reviews-or45-Udo_Island_Lighthouse_Park-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d2294035-Reviews-or55-Halla_Arboretum-Jeju_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d19175250-Reviews-or0-Gunsan_Oreum-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d6941947-Reviews-or20-Jeju_Horse_Park-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d7987808-Reviews-or20-Handam_Park-Jeju_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d2204896-Reviews-or30-Hueree_Park-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d7987797-Reviews-or20-Sarabong_Park-Jeju_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d2337362-Reviews-or5-Dolharbang_Park-Jeju_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d2204900-Reviews-or20-Ilchul_Land-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d3444592-Reviews-or5-Seobok_Park-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d2204913-Reviews-or10-Jeju_Herb_Hill-Seogwipo_Jeju_Island.html#REVIEWS',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d7987675-Reviews-or0-Geolmae_Eco_Park-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d12105688-Reviews-or0-Let_s_Run_Farm_Jeju-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297892-d8449315-Reviews-or0-Chilshimni_Poetry_Park-Seogwipo_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d8262099-Reviews-or0-Sammu_Park-Jeju_Jeju_Island.html',
    'https://www.tripadvisor.co.kr/Attraction_Review-g297885-d13343300-Reviews-or0-Let_s_Run_Park-Jeju_Jeju_Island.html'
]


for place in place_list:
    
    # declaration of area_name, location, rating, number_of_reviews, date_list, trip_type_list
    area_name = None
    location = []
    rating = []
    number_of_reviews = []
    date_list = []
    trip_type_list = []
    page_list =[]

    # url
    start = place.find('-or')
    head = place[:start+3]
    tail = place[start+3:]
    mid = tail.find('-')

    # make log 
    crawling_log = open("crawling_log.txt", 'a')

    # getting information of area
    for page in range(0, int(tail[:mid])+1, 5):

        print(str(page)+'/'+str(int(tail[:mid])))
        crawling_log.write(str(page)+'/'+str(int(tail[:mid]))+'\n')

        new_tail = str(page) + tail[mid:]
        url = head + new_tail

        driver.get(url)
        time.sleep(1)
        if driver.find_element_by_xpath('//div[@class="_36B4Vw6t"]'):
            driver.find_element_by_xpath('//div[@class="_36B4Vw6t"]').click()
            time.sleep(1)


        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
      

        # date 
        html_date_list = soup.findAll("span",{"class":"location-review-review-list-parts-EventDate__event_date--1epHa"})
        if html_date_list:
            for line in html_date_list:
                text = line.get_text()
                date_list.append(text[7:])

        # trip type
        html_trip_type_list = soup.findAll("span",{"class":"location-review-review-list-parts-TripType__trip_type--3w17i"})
        if html_trip_type_list: 
            for line in html_trip_type_list:
                text = line.get_text()
                trip_type_list.append(text[7:])

        if page == 0:
            # area_name, rating, number_of_reviews, location
            area_name = soup.find('div',{'class':'ui_columns is-multiline is-mobile'}).find('h1').get_text()
            rating.append(int(str(soup.find('div',{'class':'ui_columns is-multiline is-mobile'}).find('span',{'class':'ui_bubble_rating'}))[37:39])/10)
            number_of_reviews.append(str(soup.find('div',{'class':'ui_columns is-multiline is-mobile'}).find('span',{'class':'attractions-attraction-review-header-attraction-review-header__reviewCount--3cEMP'}).get_text())[3:])
            html_location = soup.find('div',{'class':'attractions-contact-card-ContactCard__contactRow--3Ih6v'})
            if html_location:
                location.append(html_location.get_text())

    
    # make area_name.csv
    location_df = pd.DataFrame({'location':location})
    rating_df = pd.DataFrame({'rating':rating})
    reviews_df = pd.DataFrame({'number_of_reviews':number_of_reviews})
    date_df = pd.DataFrame({'date':date_list})
    trip_df = pd.DataFrame({'trip type':trip_type_list})

    place_info = pd.concat([location_df, rating_df, reviews_df, date_df, trip_df], axis=1)
    place_info.to_csv(area_name+'.csv')

    print(str(datetime.datetime.now())+' '+area_name+' success')
    crawling_log.write(str(datetime.datetime.now())+' '+area_name+' success'+'\n')
    crawling_log.close()
    

driver.close()
print('OK')