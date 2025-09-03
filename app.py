import requests

print(requests.get("https://httpbin.org/ip").json())
resp = requests.get("https://www.google.com")
print(resp.status_code)
print(resp.text[:200])