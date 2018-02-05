import sys

def getInfo(file):
	with open(file, "r") as fd:
		content = fd.read()
	print(content)

def main():
	getInfo(sys.argv[1])
	return 1

if __name__ == "__main__":
    if (len(sys.argv) == 2):
		main()