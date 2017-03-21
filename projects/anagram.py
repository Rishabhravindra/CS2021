def detectAnagram(alist,blist):
	list1 = [0]*26
	list2 = [0]*26
	isAnagram = True

	for i in range(len(alist)):
		pos = ord(alist[i]) - ord('a')
		list1[pos] = list1[pos] + 1

	for i in range(len(blist)):
		pos = ord(blist[i]) - ord('a')
		list2[pos] = list2[pos] + 1
	j = 0	
	while j < 26 and isAnagram:
		if list1[j] == list2[j]:
			j = j + 1
		else:
			isAnagram = False
	return isAnagram

print(detectAnagram('isruhd','rishu'))


