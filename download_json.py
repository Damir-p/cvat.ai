import requests


url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
filename = "json_file.json"

response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as file:
        file.write(response.content)
        print("Файл успешно скачан.")
else:
    print("Ошибка при скачивании файла.")
