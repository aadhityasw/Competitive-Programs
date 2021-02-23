class Solution:
    def longestCommonPrefix(self, arr, n):
        sub = ""
        pos = -1
        flag = True
        while flag :
            ch = ''
            for i in range(n) :
                if len(arr[i]) > pos+1 :
                    if ch == '' :
                        ch = arr[i][pos+1]
                    else :
                        if arr[i][pos+1] != ch :
                            flag = False
                            break
                else :
                    flag = False
                    break
            pos += 1
        
        if pos <= 0 :
            return -1
        return arr[0][:pos]
