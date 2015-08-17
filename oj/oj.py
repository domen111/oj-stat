from importlib import import_module

ojlist = {"tioj"}

oj_class = {}
for i in ojlist:
	oj_class[i] = import_module("oj."+i)

def oj(ojname):
	return oj_class[ojname.lower()]

def fetch_user(judge,user):
	return set(oj(judge).fetch_user(user))