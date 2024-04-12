import requests

data = {
    'name': 'John Doe',
    'position': 'Software Engineer'
}

url = "http://127.0.0.1:5000/Post/v2/companies/1/employees"

response = requests.post(url, json=data)

print(f"Status Code: {response.status_code}")
print(f"Response Test: {response.text}")