def maxLen(n, arr):

    # A hash map to map the sum until now to the first index where the sum was encountered
    # We stert with a sum=0 at the initial index position of -1
    hash_map = {0:-1}
    summ = 0
    max_count = 0

    for i in range(n) :
        summ += arr[i]

        # If the sum is already present then the sum of elements from that position till the current position is zero
        if summ in hash_map :
            max_count = max(max_count, (i - hash_map[summ]))
        else :
            hash_map[summ] = i
        
    return max_count



if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
