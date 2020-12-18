def find_position(arr, num) :
    start = 0
    end = len(arr) - 1

    while start <= end :
        mid = (start+end)//2
        if arr[mid] > num :
            end = mid-1
        else :
            start = mid+1
        
        if start >= end :
            if arr[start] > num :
                return start
            return start+1


def find_count(num, arr, n, numberCount) :

    if num == 0 :
        return 0
    elif num == 1 :
        return numberCount[0]
    
    #index = find_position(arr, num)            # Exceeds the time limit
    index = bisect.bisect_right(arr, num)
    count = n - index

    count += numberCount[0] + numberCount[1]

    if num == 2 :
        count = count - numberCount[3] - numberCount[4]
    elif num == 3 :
        count += numberCount[2]
    
    return count


def countPairs(a,b,m,n):
    count = 0
    if n > m :
        a, b = b, a
        m, n = n, m
    b.sort()
    
    i = 0
    numberCount = [0] * 5
    while b[i] < 5 :
        numberCount[b[i]] += 1
        i += 1
    
    for num in a :
        count += find_count(num, b, n, numberCount)

    return count



import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        m,n=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        print(countPairs(a,b,m,n))
