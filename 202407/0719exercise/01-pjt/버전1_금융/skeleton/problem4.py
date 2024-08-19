import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.

def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response = requests.get(url).json()
    result = {}
    result['main'] = response['main']
    result['weather'] = response['weather']

    result['기본'] = result.pop('main')
    result['날씨'] = result.pop('weather')
    result['기본']['체감온도'] = result['기본'].pop('feels_like')
    result['기본']['지상층'] = result['기본'].pop('grnd_level')
    result['기본']['습도'] = result['기본'].pop('humidity')
    result['기본']['기압'] = result['기본'].pop('pressure')
    result['기본']['해수면'] = result['기본'].pop('sea_level')
    result['기본']['온도'] = result['기본'].pop('temp')
    result['기본']['최고온도'] = result['기본'].pop('temp_max')
    result['기본']['최저온도'] = result['기본'].pop('temp_min')
    result['날씨'][0]['요약'] = result['날씨'][0].pop('description')
    result['날씨'][0]['아이콘'] = result['날씨'][0].pop('icon')
    result['날씨'][0]['식별자'] = result['날씨'][0].pop('id')
    result['날씨'][0]['핵심'] = result['날씨'][0].pop('main')

    #켈빈 섭씨 변환 공식 : (°K − 273.15) = °C
    result['기본']['체감온도(섭씨)'] = round(result['기본']['체감온도'] - 273.15, 2)
    result['기본']['온도(섭씨)'] = round(result['기본']['온도'] - 273.15, 2)
    result['기본']['최고온도(섭씨)'] = round(result['기본']['최고온도'] - 273.15, 2)
    result['기본']['최저온도(섭씨)'] = round(result['기본']['최저온도'] - 273.15, 2)

    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '4dd99c3072833e34af376f632873c326'

    result = get_weather(api_key)
    pprint(result)
