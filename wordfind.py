text = input("Enter some text: ")

words = text.split()

for i,word in enumerate(words):
	if word.lower() == "mouse" or word.lower() == 'mice':
		print (f"Found '{word}' at position {i}")

