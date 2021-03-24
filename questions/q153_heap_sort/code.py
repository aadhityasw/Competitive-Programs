class Solution:
    def heapify(self,arr, n, i):
        '''
        :param arr: original array
        :param n: size of original array
        :param i: subtree rooted at ith index
        :return: 
        '''
        if i >= n :
            return
        
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        
        if l < n and arr[largest] < arr[l] :
            largest = l
        if r < n and arr[largest] < arr[r] :
            largest = r
        
        if largest != i :
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
        
    
    def buildHeap(self,arr,n):
        '''
        :param arr: given array
        :param n: size of array
        :return: None
        '''
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
        
        
    def HeapSort(self, arr, n):
        no = n
        
        self.buildHeap(arr, no)
        
        while no > 0 :
            arr[0], arr[no-1] = arr[no-1], arr[0]
            no -= 1
            self.heapify(arr, no, 0)
        
        
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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)
