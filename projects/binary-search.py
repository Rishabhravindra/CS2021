fruits = [1,3 , 5 , 7,9,11, 13,15,17,19,21,23]


def binarySearch (numb):
	min = 0;
	max = len(fruits) - 1
	while min <= max :
		guess = int((min + max) / 2)
		if fruits[guess] == numb :
			return guess
		elif fruits[guess] < numb:
			min = guess + 1
		elif fruits[guess] > numb:
			max = guess - 1				 
		else:
			return -1	

print ('The number was found at ' +  repr(binarySearch(132)) )


