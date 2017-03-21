from pythonds.basic.stack import Stack

def divideByTwo(num,base):
	digits = "0123456789ABCDEF"
	s = Stack()
	while num > 0:
		mod = num % base
		s.push(mod)
		num = num // base
	mystr = ''
	while not s.isEmpty():
		mystr += str(s.pop())

	return mystr


