class Solution:
    def __init__(self) :
        self.visited = []
        self.start = None
        
	def floodFill(self, image, sr, sc, newColor):
	    if self.start is None :
	        self.start = image[sr][sc]
		image[sr][sc] = newColor
		self.visited.append((sr, sc))
		if sr > 0 :
		    if image[sr-1][sc] == self.start and (sr-1, sc) not in self.visited :
		        self.floodFill(image, sr-1, sc, newColor)
		if sr < len(image)-1 :
		    if image[sr+1][sc] == self.start and (sr+1, sc) not in self.visited :
		        self.floodFill(image, sr+1, sc, newColor)
		if sc > 0 :
		    if image[sr][sc-1] == self.start and (sr, sc-1) not in self.visited :
		        self.floodFill(image, sr, sc-1, newColor)
		if sc < len(image[0])-1 :
		    if image[sr][sc+1] == self.start and (sr, sc+1) not in self.visited :
		        self.floodFill(image, sr, sc+1, newColor)
		return image







if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        image = []
        for _ in range(n):
            image.append(list(map(int, input().split())))
        sr, sc, newColor = input().split()
        sr = int(sr); sc = int(sc); newColor = int(newColor);
        obj = Solution()
        ans = obj.floodFill(image, sr, sc, newColor)
        for _ in ans:
            for __ in _:
                print(__, end = " ")
            print()
