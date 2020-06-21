from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import time
import datetime

# chrome driver 
driver = webdriver.Chrome('C:/Chrome_driver/chromedriver.exe')

# 해변
url = 'https://www.tripadvisor.co.kr/Attractions-g983296-Activities-c61-t52-Jeju_Island.html'
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

beach_list_xpath = [
    '//*[@id="ATTR_ENTRY_2487434"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_550694"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_4504781"]/div/div/div/div[1]/div[2]/a', 
    '//*[@id="ATTR_ENTRY_10126654"]/div/div/div/div[1]/div[2]/a','//*[@id="ATTR_ENTRY_7049502"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_8667339"]/div/div/div/div[1]/div[2]/a', 
    '//*[@id="ATTR_ENTRY_9583049"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_6352845"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_8790518"]/div/div/div/div[1]/div[2]/a', 
    '//*[@id="ATTR_ENTRY_10586744"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_8790487"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_9755433"]/div/div/div/div[1]/div[2]/a',
    '//*[@id="ATTR_ENTRY_19923114"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_6876755"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_6876755"]/div/div/div/div[1]/div[2]/a',
    '//*[@id="ATTR_ENTRY_16871842"]/div/div/div/div[1]/div[2]/a' 
]

# beach_list_xpath = [
#     '//*[@id="ATTR_ENTRY_2487434"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_550694"]/div/div/div/div[1]/div[2]/a', '//*[@id="ATTR_ENTRY_4504781"]/div/div/div/div[1]/div[2]/a', 
# ]


for beach in beach_list_xpath:
    # click each beach
    target = driver.find_element_by_xpath(beach)
    target.send_keys(Keys.CONTROL+'\n')
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)

    # declaration of area_name, location, rating, number_of_reviews, date_list, trip_type_list
    area_name = None
    location = []
    rating = []
    number_of_reviews = []
    date_list = []
    trip_type_list = []
    page_list =[]
    total_page = 1
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    html_total_page = soup.findAll('a',{'class':'pageNum cx_brand_refresh_phase2'})
    if html_total_page:
        for i in html_total_page:
            page_list.append(i.get_text())
        total_page = int(page_list.pop())

    print('total page:', total_page)

    # getting information of area
    for page in range(total_page):
        # click 'show more' 
        driver.find_element_by_xpath('//div[@class="_36B4Vw6t"]').click()
        time.sleep(1)

        # parser ;crawling
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
            
            # click next page
            driver.find_element_by_xpath('//*[@id="component_20"]/div[3]/div/div[8]/div/a').click()
            print('page == 0 , click')
            
        else:
            # click next page
            driver.find_element_by_xpath('//*[@id="component_19"]/div[3]/div/div[8]/div/a[2]').click()
            print('page != 0, click')
        time.sleep(3)

    # make area_name.csv
    location_df = pd.DataFrame({'location':location})
    rating_df = pd.DataFrame({'rating':rating})
    reviews_df = pd.DataFrame({'number_of_reviews':number_of_reviews})
    date_df = pd.DataFrame({'date':date_list})
    trip_df = pd.DataFrame({'trip type':trip_type_list})

    beach_info = pd.concat([location_df, rating_df, reviews_df, date_df, trip_df], axis=1)
    beach_info.to_csv(area_name+'.csv')

    
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

    # make log 
    crawling_log = open("crawling_log.txt", 'a')
    crawling_log.write(str(datetime.datetime.now())+' '+area_name+' success'+'\n')
    crawling_log.close()

    print(str(datetime.datetime.now())+' '+area_name+' success')


driver.close()
print('OK')