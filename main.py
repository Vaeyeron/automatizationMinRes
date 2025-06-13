import requests
import os

API_KEY = ''
CHART_ID = ""
CSV_FILE_PATH = r""

if not os.path.exists(CSV_FILE_PATH):
    print(f"Файл не найден: {CSV_FILE_PATH}")
    exit(1)

url = f"https://api.datawrapper.de/v3/charts/{CHART_ID}/data"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "text/csv; charset=utf-8"
}

try:
    with open(CSV_FILE_PATH, "r", encoding="utf-8") as f:
        csv_data = f.read()

    response = requests.put(url, headers=headers, data=csv_data.encode('utf-8'))

    if response.status_code in [200, 204]:
        print("Данные успешно обновлены в Datawrapper")
    else:
        print(f"Ошибка при обновлении данных: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Ошибка при чтении файла или отправке запроса: {e}")