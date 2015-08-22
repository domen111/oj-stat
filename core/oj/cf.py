import requests
import json

def fetch_user(uname):
	html = requests.get("https://codeforces.com/api/user.status?from=1&handle="+uname).text
	data = json.loads(html)
	for i in data["result"]:
		if i["verdict"] == "OK" :
			yield cf_prob((i["problem"]["contestId"], i["problem"]["index"]))

class cf_prob(tuple):
	def __repr__(self):
		if self[0] >= 100000:
			return "gym"+str(self[0])+self[1]
		else:
			return str(self[0])+self[1]
	
# by visitorIKC 15.08.18
