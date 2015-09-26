from core.oj import oj
import hashlib
import json
import pickle
import os
from time import time

_cache_dir = "core/board_cache/"

# users_probs data structure:
#   tuple(users, probs)
#   users:
#     dict(user1_name: {oj1: oj1_uid, ...}, ...)
#   probs:
#     [(prob1_judge, prob1_namestr), (prob2_judge, prob2_namestr), ...]
# return data structure:
#   dict(user1_name: [prob1_status_str, prob2_status_str, ...], ...)
def fetch(users_probs):
	users, probs = users_probs
	for i,p in enumerate(probs):
		probs[i] = (p[0], oj.decode_probname(p[0],p[1]))
	judges = set()
	for p in probs:
		judges.add(p[0])
	result = {}
	for user, accts in users.items():
		raw_result = {}
		for judge in judges:
			if judge in accts:
				raw_result[judge] = oj.fetch_user(judge,accts[judge])
			else:
				raw_result[judge] = set()
		status = []
		for p in probs:
			judge, prob = p
			if p in raw_result[judge]:
				status.append("AC")
			else:
				status.append("NO")
		result[user] = status
	return result

def _upmd5(user_probs): #user_probs md5
	return hashlib.md5(json.dumps(user_probs,sort_keys=True).encode('utf-8')).hexdigest()

def cache(user_probs, data, timeout): #timeout: minutes
	if type(user_probs) is not str:
		user_probs = _upmd5(user_probs)
	file_data = [data, time()+timeout*60]
	f = open(_cache_dir+user_probs, "wb")
	pickle.dump(file_data, f)

def load_cache(user_probs):
	if type(user_probs) is not str:
		user_probs = _upmd5(user_probs)
	f = open(_cache_dir+user_probs, "rb")
	return pickle.load(f)[0]

def update():
	for f in os.listdir(_cache_dir):
		if f.startswith("."): continue
		timeout = pickle.load(open(_cache_dir+f,"rb"))[1]
		if time()>timeout:
			os.remove(_cache_dir+f)

def fetch_auto(user_probs, timeout, force_fetch=False):
	update()
	up_md5 = _upmd5(user_probs)
	if force_fetch or not os.path.isfile(_cache_dir+up_md5):
		data = fetch(user_probs)
		cache(up_md5,data,timeout)
	else:
		data = load_cache(up_md5)
	return data