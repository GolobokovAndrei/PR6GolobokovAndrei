import requests

base_url = "http://127.0.0.1:5000/"

url_users_info = base_url + "users_info?id=1"

url_hello = base_url + "hello"

response_hello = requests.get(url_hello)

response_users_info = requests.get(url_users_info)

print(f'Hello request:\n{response_hello.text}\n\nUsers info request:\n{response_users_info.text}')