import requests

url = "http://127.0.0.1:5000/Post/v2/companies/1/employees"

response = requests.post(url)

print(response.text)