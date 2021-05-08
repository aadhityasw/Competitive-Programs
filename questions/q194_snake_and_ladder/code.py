"""
Uses a Breadth First Search approach to solve the problem, because making moves have equal probabilities,
in other words the weights between nodes are considered to be equal.
"""

class Solution:
    def minThrow(self, N, arr):
        moves = [-1]*31
        for i in range(N) :
            moves[arr[2*i]] = arr[2*i+1]
        
        visited = [False]*31
        queue = [(1, 0)]
        visited[1] = True

        while len(queue) > 0 :
            pos, step_count = queue.pop(0)
            for i in range(pos+6, pos, -1) :
                if i >= 30 :
                    return step_count + 1
                if visited[i] :
                    continue
                next_pos = moves[i] if moves[i]!=-1 else i
                queue.append((next_pos, step_count+1))
                visited[next_pos] = True


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))

