from pythonds.basic.deque import Deque

def palchecker(mystr):
	d = Deque()
	for i in mystr:
		d.addRear(i)

	isPalin = True
	while d.size() > 1 and isPalin:
		first = d.removeFront()
		sec = d.removeRear()
		if first != sec:
			isPalin = False

	return isPalin

print(palchecker("nooen"))


