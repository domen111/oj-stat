import requests
import re

def fetch_user(uid):
	#login HOJ
	login_data = {"username":"SkyOJ-BOT", "password":"1234"}
	cookies = requests.post("http://hoj.twbbs.org/judge/user/login", data=login_data).cookies

	#fetch data
	html = requests.get("http://hoj.twbbs.org/judge/user/view/"+uid, cookies=cookies).text

	#process
	html = html.split("<th>Problems</th>",1)[1].split("<td>",1)[1].split("</td>")[0]
	html = html.replace("<br>","\n").replace("&nbsp;&nbsp;&nbsp;","\n")

	for line in html.split("\n"):
		if line == "": continue
		pid = int(re.search(r"problem\/view\/(\d+)\">",line).group(1))
		if line.find('<span class="blue">') != -1:
			yield pid

def get_url(prob):
	return "http://hoj.twbbs.org/judge/problem/view/"+str(prob)
