def getData():
	groups = []
	totals=[]
	input = list((x.strip() for x in open("data//DEC01.txt", "r").readlines()))
	current = []
	for item in input:
		if item != "":
			current.append(int(item))
		else:
			groups.append(current)
			totals.append(sum(current))
			current = []
	return (groups, sorted(totals))

groups, totals = getData()

max = totals[-1]
max3 = totals[-3:]

print (max)
print (sum(max3))
