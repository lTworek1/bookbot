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
				if char.isalpha():	
					charCount.update({char:charC}) 
		

		listOfChar = []			
		for char in charCount:
			count = charCount[char]
			charDict = {"char": char, "count":count}
			listOfChar.append(charDict)
 
		def sort_on(dict):
			return dict["count"]
		
		listOfChar.sort(reverse=True, key=sort_on)

		print(f'--- Begin report of {filePath} ---')
		print(f'{countW} words found in the document')
		print('')
		for charDict in listOfChar:
			char = charDict["char"]
			countC = charDict["count"]
			print(f"The '{char}' character was found {countC} times")

		print('--- End report ---')


main()
