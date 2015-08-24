import requests
import re

def fetch_user(uname):
	html = requests.get("http://tioj.ck.tp.edu.tw/users/"+uname).text

	html = html.split("<tbody>",1)[1].split("</tbody>")[0]
	html = html.replace("<tr>","").replace("</tr>","")
	html = html.replace("<td>","").replace("</td>","")
	html = re.sub(r" {2,}","",html)
	html = re.sub(r"\n{2,}","\n",html)

	for line in html.split("\n"):
		if line == "": continue
		pid = int(re.search(r"problems\/(\d+)\/submissions",line).group(1))
		if line.find("text-success") != -1:
			yield pid

def get_url(prob):
	return "http://tioj.ck.tp.edu.tw/problems/"+str(prob)
