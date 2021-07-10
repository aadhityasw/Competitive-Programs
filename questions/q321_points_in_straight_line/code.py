class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def computeGCD(self, x, y):
        if x > y:
            small = y
        else:
            small = x
        gcd = 1
        for i in range(1, small + 1):
            if ((x % i == 0) and (y % i == 0)):
                gcd = i
        return gcd

    def maxPoints(self, A, B):
        N = len(A)
        if N <= 2:
            return N
        max_points = 0

        for i in range(N):
            hash_map = {}

            horizontal = 0
            vertical = 0
            overlap = 1

            x1, y1 = A[i], B[i]
            for j in range(i + 1, N):
                x2, y2 = A[j], B[j]
                if x1 == x2 and y1 == y2:
                    overlap += 1
                elif x1 == x2:
                    vertical += 1
                elif y1 == y2:
                    horizontal += 1
                else:
                    dy = y2 - y1
                    dx = x2 - x1
                    slope = 1.0* dy / dx
                    if slope in hash_map:
                        hash_map[slope] = hash_map[slope] + 1
                    else:
                        hash_map[slope] = 1
            curr_max = max(list(hash_map.values()) + [vertical, horizontal])
            curr_max += overlap
            max_points = max(max_points, curr_max)
        return max_points
