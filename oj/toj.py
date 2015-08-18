import requests
import json

def fetch_user(uid):
	data = requests.post("http://toj.tfcis.org/oj/be/api", data={"reqtype":"AC", "acct_id":uid})
	data = json.loads(data.text)
	return data["ac"]
