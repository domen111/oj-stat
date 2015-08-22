import sys
from core.oj import oj

def _fetch(judge_user):
	judge,user = judge_user.split(":",1)
	return oj.fetch_user(judge,user)

def compare(expression): #todo
	return _fetch("tioj:visitorIKC") - _fetch("tioj:domen111") #debug

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Error: miss expression")
		print("See README.md for help")
		sys.exit()
	expression = sys.argv[1]
	result = list(compare(expression))
	result.sort()
	print("%d problems in total\n"%len(result))
	for prob in result:
		print(prob[0] + " " + str(prob[1]), end="\t")
	print()
