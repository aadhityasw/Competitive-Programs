"""
This code is wrong and is thus incomplete.
"""


class Solution:
	def findMidSum(self, ar1, ar2, n): 
		
		f1 = 0
		r1 = n-1
		f2 = 0
		r2 = n-1
		
		while f1 <= r1 and f2 <= r2 :
		    mid1 = (f1 + r1) // 2
		    mid2 = (f2 + r2) // 2
		    print(ar1[mid1], ar2[mid2])
		    if ar1[mid1] > ar2[mid2] :
		        r1 = mid1-1
		        f2 = mid2
		    elif ar1[mid1] < ar2[mid2] :
		        f1 = mid1
		        r2 = mid2-1
		    else :
		        return ar1[mid1] + ar2[mid2]
		  
		    if f1 == r1-1 and f2 == r2-1 :
		        return max(ar1[f1], ar2[f2]) + max(ar1[r1], ar2[r2])
		    elif f1 == r1 and f2 == r2 :
		        return ar1[f1] + ar2[f2]
