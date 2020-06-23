import pandas as pd

beach_list = [
    '용머리 해안','함덕 서우봉 해변','협재 해수욕장','월정리해변','중문 색달 해변','금능해수욕장','김녕 성세기 해변',
    '광치기 해변','세화 해수욕장','이호테우해변','표선해비치해변','곽지해수욕장','소금막해변','삼양 검은모래 해변','산호해수욕장'
]

mountain_list = ['한라산 국립공원','성산 일출봉','송악산','새별오름','따라비 오름','민오름 -  오라동','산방산', '궷물오름']

park_list = [
    '생각하는 정원','비자림','제주 절물 자연 휴양림','한림공원','제주 돌문화 공원','제주 4.3 평화공원','제주 여미지 식물원',
    '우도등대공원','한라 수목원','군산오름','조랑말 체험공원','한담공원','휴애리 자연 생활 공원','사라봉공원','돌하르방 공원',
    '일출 랜드','서복 공원','제주 허브 동산','걸매생태공원','렛츠런팜 제주','칠십리 시 공원','삼무공원','렛츠런파크제주'
]

place_list = []
# place_list.append(beach_list)
place_list.append(mountain_list)
# place_list.append(park_list)


place_info = None

for place in place_list:
    for area in place:
        data = pd.read_csv(area+'.csv', sep=',', dtype='unicode')
        # place_info = pd.concat([data], axis=1)

place_info.to_csv('place_info.csv')