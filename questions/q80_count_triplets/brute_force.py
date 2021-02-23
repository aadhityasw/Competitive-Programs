class Solution:
	def countTriplet(self, arr, n):
		arr.sort()
		count = 0
		for i in range(n) :
		    k = i+1
		    for j in range(i+1, n) :
		        if (arr[i]+arr[j]) in arr[k:] :
		            k = arr.index(arr[i]+arr[j])
		            count += 1
		return count
