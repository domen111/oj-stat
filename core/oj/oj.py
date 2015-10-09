from importlib import import_module

ojlist = {"tioj","toj","hoj","cf"}

oj_class = {}
for i in ojlist:
	oj_class[i] = import_module("core.oj."+i)

def oj(ojname):
	return oj_class[ojname.lower()]

def fetch_user(judge,user):
	ac = oj(judge).fetch_user(user)
	ac = map(lambda pid:(judge,pid),ac)
	return set(ac)

def get_url(prob):
	judge, pid = prob
	if hasattr(oj_class[judge], "get_url"):
		return oj_class[judge].get_url(pid)
	else:
		return None

def decode_probname(judge,prob):
	if hasattr(oj_class[judge], "decode_probname"):
		return oj_class[judge].decode_probname(prob)
	elif prob.isdigit():
		return int(prob)
	else:
		return prob
