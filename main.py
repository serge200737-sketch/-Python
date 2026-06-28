import requests

print("Запрашиваю случайную шутку...")
response = requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()

print(f"Сетап: {data['setup']}")
print(f"Панчлайн: {data['punchline']}")