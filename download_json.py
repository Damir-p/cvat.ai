import requests

json_url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"

response = requests.get(json_url)
data = response.json()

with open("deviation.json", "w") as file:
    file.write(response.text)

print("JSON file downloaded successfully.")
