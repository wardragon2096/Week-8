def printAll(seq):
	if seq:
		print(seq[0])
		printAll(seq[1:])
printAll("Here is Lees Theory!")
printAll((1,2,3,4,5,6,7,8))
printAll([9,8,7,6,5,4,3,2,1])
