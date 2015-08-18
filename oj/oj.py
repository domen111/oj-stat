from importlib import import_module

ojlist = {"tioj","toj"}

oj_class = {}
for i in ojlist:
	oj_class[i] = import_module("oj."+i)

def oj(ojname):
	return oj_class[ojname.lower()]

def fetch_user(judge,user):
	ac = oj(judge).fetch_user(user)
	ac = map(lambda pid:(judge,pid),ac)
	return set(ac)