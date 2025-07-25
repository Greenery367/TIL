import requests

url = "https://api.openweathermap.org/data/2.5/weather?lat=37.56&lon=126.97&appid=5f809c1f484a2216568b1803f184b61d"
data = requests.get(url).json()
print(data)