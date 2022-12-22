import requests

url = "http://localhost:3000/api/v1/prescriptions"
headers = {"Content-Type": "application/json"}
pay_load = {"token": 7067506, }

response = requests.get(url, json=pay_load)

print(response.status_code)
print(response.json())


def check_token(token):
    response = requests.get(url, json=token)
    print(response)
    return response
