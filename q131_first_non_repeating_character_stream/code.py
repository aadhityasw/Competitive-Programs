class Solution:
	def FirstNonRepeating(self, A):
		arr = [0] * 26
		first = None
		st = ""
		queue = []
		
		for ch in A :
		    arr[ord(ch)-97] += 1
		    if arr[ord(ch)-97] == 1 :
		        if first is None :
		            first = ch
		        else :
		            queue.append(ch)
		    elif arr[ord(ch)-97] > 1 and first == ch :
		        if len(queue) == 0 :
		            first = None
		        else :
		            while len(queue) > 0 :
		                first = queue.pop(0)
		                if arr[ord(first)-97] > 1 :
		                    if len(queue) == 0 :
		                        first = None
		                        break
		                    continue
		                else :
		                    break
		    
		    if first :
		        st += first
		    else :
		        st += '#'
		
		return st


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)
