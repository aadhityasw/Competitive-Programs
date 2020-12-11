# This solves in O(N^2) time complexity

"""

Here we take a number and then check if we can get two other numbers from the array with the matching sum

"""


class Solution:
	def countTriplet(self, arr, n):
		arr.sort()
		i = n-1
		count = 0
		while i >= 2 :
			j = 0
			k = i - 1
			while j < k :
				if arr[j] + arr[k] == arr[i] :
					count += 1
					j += 1
				elif arr[j] + arr[k] > arr[i] :
					k -= 1
				else :
					j += 1
			i -= 1
		return count
