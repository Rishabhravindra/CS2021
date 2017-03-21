
from pythonds.basic.stack import Stack
def checkPar(mystr):
	index = 0
	s = Stack()
	#loop through the string 
	isBal = True
	while isBal and index < len(mystr):
		if mystr[index] == "(":
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

def checkMulPar(mystr):
	index = 0
	isBal = True
	s = Stack()
	while index < len(mystr) and isBal:
		sym = mystr[index]
		if sym in "({[":
			s.push(sym)
		else:
			if s.isEmpty():
				isBal = False
			else:
				top = s.pop()
				if not isMatch(top, sym):
					isBal = False
		index = index + 1
	if isBal and s.isEmpty():
		return True
	else:
		return False
def isMatch(open, close):
	opens = "({["
	closers = ")}]"
	return opens.index(open) == closers.index(close)	
print (checkMulPar('{{([][])}()}'))
print (checkMulPar('[{()]'))

