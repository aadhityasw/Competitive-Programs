class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        table = []

        left = 0
        for i, num in enumerate(A) :
            if len(table) > 0 :
                table[-1][2] = i-1
            if num % 2 == 1 :
                table.append([left, i, 0])
                left = i+1
        if len(table) > 0 :
            table[-1][2] = n-1

        if B == 0 :

            if len(table) == 0 :
                return (2 ** n)-1

            count = 0
            for (l, p, r) in table :
                count += (2 ** (p - l))-1
            count += (2 ** (n-1-table[-1][1])-1)
            return count

        
        #print(table)
        
        front = 0
        rear = B-1
        count = 0
        while front <= rear and rear < len(table) :
            num_left = table[front][1] - table[front][0]
            num_right = table[rear][2] - table[rear][1]
            if num_left > 0 and num_right > 0 :
                count += ((num_left+1) * (num_right+1))
            elif num_left > 0 :
                count += num_left + 1
            else :
                count += num_right + 1
            front += 1
            rear += 1
            #print(front, rear, count)
        
        return count

        