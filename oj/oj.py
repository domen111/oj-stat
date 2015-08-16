ojlist = {"tioj"}

oj = {}
for i in ojlist:
	oj[i] = __import__(i).oj
