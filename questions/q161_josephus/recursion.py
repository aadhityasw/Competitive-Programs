class Solution:
    def recursiveEliminate(self, arr, s, k) :
        if len(arr) == 1 :
            return arr[0]

        s = (s + k - 1) % len(arr)
        arr.pop(s)
        return self.recursiveEliminate(arr, s, k)


    def josephus(self,n,k):
        return self.recursiveEliminate([i for i in range(1, n+1)], 0, k)
