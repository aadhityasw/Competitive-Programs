class Solution:

    def findHcf(self, a, b) :
        """
        Given two numbers, returns their HCF
        """
        if a < b :
            return self.findHcf(b, a)
        
        if b == 0 :
            return a
        return self.findHcf(b, a%b)
    

    def findTime(self, word) :
        """
        Finds the time t of rotation cycle
        """

        # Find the position of the start of the recurring string
        recurring_pos = (word+word).find(word, 1, -1)

        # If there is no recurring string in there (word does not occur the same before n*(n+1)/2 iterations)
        if recurring_pos == -1 :
            pos = len(word)
        # If there is a recurring occurance
        else :
            pos = recurring_pos
        
        # Find the time stamp where we wil get the same word
        for i in range(1, 2*pos+1):
            if ((i*(i+1))//2)%pos == 0:
                return i
        return -1

    
    # @param A : list of strings
    # @return an integer
    def solve(self, A):

        time = []
        for st in A :
            time.append(self.findTime(st))
        
        lcm = 1
        for t in time :
            lcm = ((lcm * t) // self.findHcf(lcm, t))
        
        return lcm % 1000000007
