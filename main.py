import sys
def main():
	try:
		filePath = sys.argv[1]
	except:
		filePath = input("File Path: ")	
	
	with open(filePath) as f:
		file_contents = f.read()
		# print(file_contents)

		words = file_contents.split()
		countW = 0
		for word in words:

			countW += 1

		print(f'In this file is {countW} words')


main()
