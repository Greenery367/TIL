import requests

url = "https://api.openweathermap.org/data/2.5/weather?lat=37.56&lon=126.97&appid={API key}"
data = requests.get(url).json()
print(data)