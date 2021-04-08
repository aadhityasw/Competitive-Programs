class Solution:
    def UncommonChars(self,A, B):
        boardA = [0]*26
        boardB = [0]*26
        
        for i in A :
            boardA[ord(i)-97] += 1
        for i in B :
            boardB[ord(i)-97] += 1

        ans = ""
        
        for i in range(26) :
            if (boardA[i] > 0 and boardB[i] > 0) or (boardA[i] == boardB[i] == 0) :
                continue
            else :
                ans += chr(i+97)
        
        if len(ans) == 0 :
            return -1
        
        return ans







if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))
