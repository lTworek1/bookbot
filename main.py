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
		charCount = {}
		for word in words:

			countW += 1
			
			lowWord = word.lower()
			for char in lowWord:
				try:
					charC = charCount[char]
				except:
					charC = 0
				
				charC += 1	
				charCount.update({char:charC}
) 
		print(f'In this file is {countW} words')
		print('Characters Count:')
		printStr = ""
		for char in sorted(charCount):
			countC = charCount[char]
			printStr = f'{printStr}["{char}"]: {countC}; '
		
		print(printStr)


main()
