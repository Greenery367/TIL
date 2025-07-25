from pprint import pprint
import requests

def get_seoul_weather():
    # API KEY
    API_KEY = "5f809c1f484a2216568b1803f184b61d"
    
    # 서울의 위도와 경도
    lat = 37.56
    lon = 126.97
    
    # 도시 이름
    city_name = "Busan,KR"
    
    url1 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    url2 = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    
    # API 요청 보내기
    response = requests.get(url1).json()
    return response

result = get_seoul_weather()
print(result)