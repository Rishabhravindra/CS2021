from math import *
alist = [
24.72,	 	25.74,	 	26.38,	 	26.55,	 	26.79,	 	27.28,	 	27.44	 ,	27.67,	 	27.87	 ,	27.96,
28.10,	 	28.17,	 	28.41,	 	28.62,	 	28.63,	 	29.00,	 	29.24	, 	29.26,	 	29.50	 ,	30.44]

for i in range(len(alist)):
	# count += alist[i]
	# sumOfOf += pow(alist[i],2)
	alist[i] = abs(28.03 - alist[i])/0.6745
print(round((alist[9]+alist[10])/2,3))

count = 0
sumOfSq = 0
sumOfOf = 0
for i in range(len(alist)):
	count += alist[i]
	sumOfOf += pow(alist[i],2)

sumOfSq = pow(count, 2)/20;

shu = (sumOfOf - sumOfSq)/19
print(round(sqrt(shu),3))
