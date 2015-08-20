import requests
import json

def fetch_user(uname):
	html = requests.get("https://codeforces.com/api/user.status?from=1&handle="+uname).text
	data = json.loads(html)
	for i in data["result"]:
		if i["verdict"] == "OK" :
			yield str(i["problem"]["contestId"]) + str(i["problem"]["index"])
	
# by visitorIKC 15.08.18
