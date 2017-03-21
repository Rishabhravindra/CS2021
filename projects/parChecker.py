
from pythonds.basic.stack import Stack
def checkPar(mystr):
	index = 0
	s = Stack()
	#loop through the string 
	isBal = True
	while isBal and index < len(mystr):
		for i in mystr:
			if i == "(":
				s.push("(")
			else:
				if s.isEmpty():
					isBal = False
				else:
					s.pop()

		index = index + 1
	if isBal and s.isEmpty():
		return True
	else:
		return False

print (checkPar('((()))'))
print (checkPar('(()'))