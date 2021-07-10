class Solution:
	def singleNumber(self, nums):
		xor = 0
		for n in nums :
			xor = xor ^ n
		
		first = 0
		second = 0
		# Find the two's complement of the overall xor
		val = xor & (- xor)
		for n in nums :
			if n & val :
				first = first ^ n
			else :
				second = second ^ n
		
		ans = [first, second]
		ans.sort()
		return ans



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int,input().split()))
        ob = Solution();
        ans = ob.singleNumber(v)
        for i in ans:
            print(i, end = " ")
        print()
