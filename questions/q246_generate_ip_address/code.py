
class Solution:

    def generate(self, s, level, prev) :
        """
        Utility function to generate and print IP address from given string.

        Parameters
        ----------
        s - the remaining string left to create IP addresses
        level - the current level we are in, it ranges from 0 to 4 for IpV4 format
        prev - the portion of generated ip address generated until now
        """

        # Base Case
        if level == self.totalLevels :
            # If the string starts with 0 but the number is not zero we return
            # If the number is greater than 255, we return
            if int(s) >= 256 or (s[0] == '0' and len(s) > 1) :
                return
            self.ans.append((prev + s))
            return
        
        # Take i characters from s for every iteration
        for i in range(1, (len(s)-(self.totalLevels - level) + 1)) :
            # If the string starts with 0 but the number is not zero we return
            if s[0] == '0' and i > 1  :
                return
            # We proceed only if we have extracted a number in appropriate range for current level
            if int(s[:i]) < 256 :
                self.generate(s[i:], level+1, (prev + s[:i] + '.'))


    def genIp(self, s):
        self.ans = []
        self.totalLevels = 4
        self.generate(s, 1, "")
        return self.ans


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        for u in res:
            print(u)
