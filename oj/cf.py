import urllib.request
import requests
import json

def fetch_user(uname):
	with urllib.request.urlopen("https://codeforces.com/api/user.status?from=1&handle="+uname) as response:
		html = response.read().decode("utf-8")
	data = json.loads(html)
	ret = set()
	for i in data["result"]:
		if i["verdict"] == "OK" :
			l = str()
			if i["problem"]["contestId"] < 10:
				l = "  " + str(i["problem"]["contestId"])
			elif i["problem"]["contestId"] < 100:
				l = " " + str(i["problem"]["contestId"])
			else:
				l = "" + str(i["problem"]["contestId"])
			ret.add(str(l) + str(i["problem"]["index"]))
	return ret
	
# by visitorIKC 15.08.18
