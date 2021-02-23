'''
:param x: value to be inserted
:return: None

queue_1 = [] # first queue
queue_2 = [] # second queue
'''


def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    queue_1.append(x)
    

def pop():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    
    while len(queue_1) > 1 :
        queue_2.append(queue_1.pop(0))
    
    element = -1
    if len(queue_1) == 1 :
        element = queue_1.pop(0)
    
    while len(queue_2) > 0 :
        queue_1.append(queue_2.pop(0))

    return element


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

queue_1 = [] # first queue
queue_2 = [] # second queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
