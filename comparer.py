import sys
from oj import oj

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Error: miss expression")
		print("See README.md for help")
		sys.exit()
	expression = sys.argv[1]