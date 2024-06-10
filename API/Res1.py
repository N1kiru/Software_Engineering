import requests

stadiums_location = {
    "Лужники": "37.554191,55.715551",
    "Спартак": "37.440262,55.818015",
    "Динамо": "37.559809,55.791540"
}

api_key = '6fd12c2a-d875-4620-854a-1fae711a6f4d'

points = ""
for stadium, coords in stadiums_location.items():
    points += f"{coords},pm2dgl~"

points = points.rstrip("~")

map_url = (
    "https://static-maps.yandex.ru/1.x/"
    f"?apikey={api_key}"
    "&l=map"
    f"&pt={points}"
    "&z=11&size=650,450"
)

response = requests.get(map_url)

print("Изображение сохранено")
with open("moscow_with_points.png", "wb") as file:
    file.write(response.content)
print(response.status_code)