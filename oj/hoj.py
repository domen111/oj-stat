import requests
import re

def fetch_user(uid):
	html = requests.get("http://hoj.twbbs.org/judge/user/view/"+uid).text

	html = html.split("<th>Problems</th>",1)[1].split("<td>",1)[1].split("</td>")[0]
	html = html.replace("<br>","\n").replace("&nbsp;&nbsp;&nbsp;","\n")
	print(html,file=open("test.html",'w'))

	for line in html.split("\n"):
		if line == "": continue
		pid = int(re.search(r"problem\/view\/(\d+)\">",line).group(1))
		if line.find('<span class="blue">') != -1:
			yield pid
