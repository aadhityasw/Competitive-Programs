# Codechef -  SORTVS

# Incomplete

testcases = int(input())
for tes in range(testcases) :
	(n, m) = map(int, input().strip().split(' '))
	arr = list(map(int, input().strip().split(' ')))
	mdict = {}
	marr = []
	for i in range(m) :
		(x, y) = map(int, input().strip().split(' '))
		marr.append([x, y])
		if x in mdict :
			mdict[x].add(y)
		else :
			mdict[x] = set()
			mdict[x].add(y)
		if y in mdict :
			mdict[y].add(x)
		else :
			mdict[y] = set()
			mdict[y].add(x)
	if m == 0 :
		numswaps = 0
		i = 0
		while(i<n) :
			if arr[i] == (i+1) :
				i += 1
			else :
				y = arr[i]-1
				arr[i], arr[y] = arr[y], arr[i]
				numswaps += 1
		print(numswaps)
	else :
		for (i, j) in marr :
			if arr[i-1] != i and arr[j-1] != j :
				arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
		numswaps = 0
		i = 0
		while(i<n) :
			if arr[i] == (i+1) :
				i += 1
			else :
				y = arr[i]-1
				arr[i], arr[y] = arr[y], arr[i]
				if (y+1) in mdict and (i+1) in mdict[y+1] :
					continue
				else :
					numswaps += 1
		print(numswaps)