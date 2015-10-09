import requests
import json
import re

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
	
def get_url(prob):
	cid, pid = prob
	if cid < 100000:
		return "http://codeforces.com/problemset/problem/"+str(cid)+"/"+pid
	else:
		return "http://codeforces.com/gym/"+str(cid)+"/problem/"+pid

def decode_probname(prob):
	regex_result = re.search(r"(\d+)([A-Z])",prob)
	return (regex_result.group(1),regex_result.group(2))
