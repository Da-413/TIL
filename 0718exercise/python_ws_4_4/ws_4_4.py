import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'

dummy_data = []

for i in range(10):
    response = requests.get(API_URL)
    parsed_data = response.json()
    
    dummy_data.append({'company': parsed_data[i]['company']['name'],
                       'lat': parsed_data[i]['address']['geo']['lat'],
                       'lng': parsed_data[i]['address']['geo']['lng'],
                       'name': parsed_data[i]['name']})
    


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(lst):

    censored_user_list = {}

    for data in lst:

        company = data['company']
        name = data['name']

        if censorship(company, name):
            if company not in censored_user_list:
                censored_user_list[company] = [name]
            else:
                censored_user_list[company].append(name)
    
    return censored_user_list


def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True
    
print(create_user(dummy_data))