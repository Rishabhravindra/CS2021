from pythonds.basic.stack import Stack

def divideByTwo(num):
	s = Stack()
	while num > 0:
		mod = num % 2
		s.push(mod)
		num = num // 2
	mystr = ''
	while not s.isEmpty():
		mystr += str(s.pop())

	return mystr

divideByTwo(233)

