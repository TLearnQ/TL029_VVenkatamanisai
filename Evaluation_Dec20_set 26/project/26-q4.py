import requests

Authorization={"Authorization": "Bearer reqres-token"}
payload={ "name": "trinity", "job": "operator"} 

url ="https://reqres.in/api/users"
responses = requests.post(url,payloads=payload,Authorization=Authorization)

print("Status Code:", responses.status_code)
print("Response:", responses.json())
