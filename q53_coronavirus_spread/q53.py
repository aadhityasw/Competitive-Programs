# CodeChef - COVID19

testcases = int(input())
for test in range(testcases) :
	n = int(input())
	x = list(map(int, input().strip().split(' ')))
	mins = n
	maxs = 1
	i = 1
	p = 1
	while(i < n) :
		if (x[i] - x[i-1]) <= 2 : 
			p += 1
		else :
			if p > maxs :
				maxs = p
			if p < mins :
				mins = p
			p = 1
		i += 1
	if p > maxs :
		maxs = p
	if p < mins :
		mins = p
	print(mins, maxs)