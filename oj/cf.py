import requests
import json

def fetch_user(uname):
	html = requests.get("https://codeforces.com/api/user.status?from=1&handle="+uname).text
	data = json.loads(html)
	for i in data["result"]:
		if i["verdict"] == "OK" :
			l = str()
			if i["problem"]["contestId"] < 10:
				l = "     " + str(i["problem"]["contestId"])
			elif i["problem"]["contestId"] < 100:
				l = "    " + str(i["problem"]["contestId"])
			elif i["problem"]["contestId"] < 1000:
				l = "   " + str(i["problem"]["contestId"])
			else:
				l = "" + str(i["problem"]["contestId"])
			yield str(l) + str(i["problem"]["index"])
	
# by visitorIKC 15.08.18
