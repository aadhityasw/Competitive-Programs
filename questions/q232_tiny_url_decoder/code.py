class Solution:
	def idToShortURL(self,n):
		url = ""
		num = n
		
		while num > 0 :
		    a = num % 62
		    num = num // 62
		    
		    if a < 26 :
		        ch = chr(a + 97)
		    elif a < 52 :
		        ch = chr(a + 65 - 26)
		    else :
		        ch = chr(a + 48 - 52)
		    
		    url = ch + url
		
		return url


def shortURLToId(shortURL):
    id = 0
    for i in shortURL:
        val_i = ord(i)
        if (val_i >= ord('a') and val_i <= ord('z')):
            id = id * 62 + val_i - ord('a')
        elif (val_i >= ord('A') and val_i <= ord('Z')):
            id = id * 62 + val_i - ord('A') + 26
        else:
            id = id * 62 + val_i - ord('0') + 52
    return id


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        url = ob.idToShortURL(n)
        print(url)
        print(shortURLToId(url))
        tc -= 1
