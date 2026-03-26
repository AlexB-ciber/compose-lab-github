import requests

r = requests.get("http://app:8010")
if r.status_code == 200:     print("TEST OK")
else:
    print("TEST FAIL")
