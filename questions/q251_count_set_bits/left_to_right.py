class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        num_ones = [1]
        b = 2
        for i in range(1, 32) :
            num_ones.append(2*num_ones[-1] + b)
            b = b * 2
        #print(num_ones)


        binary = bin(A)[2:]
        n = len(binary)
        count = 0
        cur_ones = 0

        for i, ch in enumerate(binary) :
            if ch == '1' :
                b = n - i - 1
                count = (count + (cur_ones * (2 ** b)) + (num_ones[b-1] if b > 0 else 0)) % 1000000007
                cur_ones += 1
            #print(count)
        count += cur_ones
        
        return count
