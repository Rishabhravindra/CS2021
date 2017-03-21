from pythonds.basic.queue import Queue

def hotPotato(numlist, ctr):
	q = Queue()

	for i in numlist:
		q.enqueue(i)

	while q.size() > 1:
		for e in range(ctr):
			q.enqueue(q.dequeue())

		q.dequeue()

	return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))



