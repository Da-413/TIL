import requests

def get_sunday_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{city}의 현재 날씨 정보:")
        print(f"기온: {data['main']['temp']} °C")
        print(f"습도: {data['main']['humidity']} %")
        print(f"날씨 상태: {data['weather'][0]['description']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# API 키와 서울의 도시명 설정
api_key = '4dd99c3072833e34af376f632873c326'  # 본인의 openweathermap API 키로 대체해야 합니다
city = 'Seoul'

get_sunday_weather(api_key, city)

# 실행결과  : 
# $ python problem5.py 
# Seoul의 현재 날씨 정보:
# 기온: 31.19 °C
# 습도: 62 %
# 날씨 상태: scattered clouds