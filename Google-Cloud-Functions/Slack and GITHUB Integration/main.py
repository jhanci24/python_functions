import requests
from requests.structures import CaseInsensitiveDict

def my_func():
	print("slack with gitwebhooks")
	url = "https://hooks.slack.com/services/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"
	headers = CaseInsensitiveDict()
	headers["Content-type"]= "application/json"
	data = '{"text":"GITHUB code is committed"}'
	resp = requests.post(url,headers=headers, data=data)
	print(resp.status_code)
	return f"Hellow World" 
my_func()