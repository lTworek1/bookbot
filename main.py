import sys
def main():
	try:
		filePath = sys.argv[1]
	except:
		filePath = input("File :Path: ")	

	with open(filePath) as f:
		file_contents = f.read()
		print(file_contents)
main()
