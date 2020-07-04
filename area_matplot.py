import matplotlib.pyplot as plt
import csv
import pandas as pd
from matplotlib import font_manager, rc

rc('font', family='Han Santteut Dotum')

place_list = [
    # beach
    '용머리 해안','함덕 서우봉 해변','협재 해수욕장','월정리해변','중문 색달 해변'
    # '금능해수욕장','김녕 성세기 해변','광치기 해변','세화 해수욕장','광치기 해변',
    # '이호테우해변','표선해비치해변','곽지해수욕장','소금막해변','삼양 검은모래 해변',
    # '산호해수욕장',
    # # mountain
    # '한라산 국립공원','성산 일출봉','송악산','산방산','새별오름','따라비 오름',
    # '민오름 -  오라동','궷물오름','생각하는 정원',
    # #park
    # '비자림','제주 절물 자연 휴양림','한림공원','제주 돌문화 공원','제주 4.3 평화공원',
    # '제주 여미지 식물원','우도등대공원','한라 수목원','군산오름','조랑말 체험공원',
    # '한담공원','휴애리 자연 생활 공원','사라봉공원','돌하르방 공원','일출 랜드',
    # '서복 공원','제주 허브 동산','걸매생태공원','렛츠런팜 제주','칠십리 시 공원',
    # '삼무공원','렛츠런파크제주'
]
type_list = ['친구와 여행함','나 혼자 여행함','가족과 여행함','커플로 여행함']

month_info = []


def plot(date_month_list,trip_type_list):
    ax1 = plt.subplot(131)
    graph1 = plt.hist(date_month_list, range=(1,13), bins=12)
    if plt.hist(trip_type_list):
        ax2 = plt.subplot(132)
        graph1 = plt.hist(trip_type_list)
    plt.title(place)

    # plt.show()
    plt.savefig(place+'.png')

for place in place_list:
    f = open('./_data/place/'+place+'.csv', 'r', encoding='utf-8')
    data = pd.read_csv(f)
    location = [list(data['location'])[0]]
    rating = [list(data['rating'])[0]]
    area_name = [place]

    feature_date = data['date']
    feature_trip_type = data['trip type']
    date_list = []
    date_month_list = []
    trip_type_list = []
    month_count = []
    type_count = []


    for date in list(feature_date):
        if isinstance(date,float):
            break
        else:
            date_list.append(date)


    for trip_type in list(feature_trip_type):
        if isinstance(trip_type,float):
            break
        else:
            trip_type_list.append(trip_type)


    for date in date_list:
        date_month_list.append(int(date[6:-1]))

    for month in range(13):
        month_count.append(date_month_list.count(month))
    
    for trip_type in range(4):
        type_count.append(trip_type_list.count(trip_type))

    plot(date_month_list,trip_type_list)


    """
    # the most traveled month
    month_index = []
    month_max = max(month_count)
    
    for i, v in enumerate(month_count):
        if v == month_max:
            month_index.append(i)
    
    print(place,",",month_index)
    
    
    area_name_df = pd.DataFrame({'area name':area_name})
    location_df = pd.DataFrame({'location':location})
    rating_df = pd.DataFrame({'rating':rating})
    month_df = pd.DataFrame({'month':month_index})

    month_info.append(pd.concat([area_name_df,location_df,rating_df,month_df], axis=1))
    add_df = month_info


merge_data = pd.concat(month_info, axis = 0, ignore_index = True)
merge_data.to_csv('area_data_with_most_visited_month.csv', index = False)

"""