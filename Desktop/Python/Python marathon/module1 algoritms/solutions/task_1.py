


list1 = []
n = 3
k = 7
s = 0

while len(list1) <= k:
	if len(list1) == 0:
		list1.append(n**s)
		s += 1
	else:
		list1.append(n**s)
		a = list1[-1]
		for i in list1:
			if i == a:
				break
			else:
				list1.append(a+i)
		s+=1

print(list1)

print(list1[k - 1])

