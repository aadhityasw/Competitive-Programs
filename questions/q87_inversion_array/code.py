def merge_sort_and_count(arr, start, end) :
    count = 0

    if start >= end :
        return 0
    
    # Splitting Process
    mid = (start + end) // 2
    count += merge_sort_and_count(arr, start, mid)
    count += merge_sort_and_count(arr, mid+1, end)

    # Merging Process
    temp = []
    i = start
    j = mid+1
    while i <= mid and j <= end :
        if arr[i] > arr[j] :
            count += mid-i+1
            temp.append(arr[j])
            j += 1
        else :
            temp.append(arr[i])
            i += 1
    
    while i <= mid :
        temp.append(arr[i])
        i += 1
    while j <= end :
        temp.append(arr[j])
        j += 1
    
    for i in range(len(temp)) :
        arr[start+i] = temp[i]
    
    return count


def inversionCount(a,n):
    count = merge_sort_and_count(a, 0, n-1)
    return count



import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(inversionCount(a,n))
