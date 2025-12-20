import requests

api_url = "https://reqres.in/api/users"
headers = {
    "Authorization": "Bearer reqres-token"
}

payload = {
    "name": "trinity",
    "job": "operator"
}

response = requests.post(api_url, json=payload, headers=headers)

response_data = response.json()

# Count number of fields in the response
field_count = len(response_data)

print("Status Code:", response.status_code)
print("Response JSON:", response_data)
print("Number of fields returned:", field_count)
