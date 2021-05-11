path_length = {}


def findPath(i, Parr, n) :
    
    global path_length
    if path_length[i] == 0 :
        for j in range(i+1, n) :
            if Parr[j].a > Parr[i].b :
                leng = 1 + findPath(j, Parr, n)
                path_length[i] = max(path_length[i], leng)
    
    return path_length[i]



def maxChainLen(Parr, n):
    Parr.sort(key= lambda x : x.a)

    global path_length
    path_length = [0] * n
    path_length[-1] = 1

    i = 0
    max_len = 0
    while i < (n - max_len) :
        max_len = max(max_len, findPath(i, Parr, n))
        i += 1

    return max_len
    


class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        print(maxChainLen(Parr, n))
