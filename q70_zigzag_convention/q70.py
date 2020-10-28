class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """ Solution obtained by visiting one row at a time. """
        
        encoded_string = ""

        # Edge case
        if len(s) <= numRows or numRows == 1:
            return (s)

        # First row
        ind = 0
        while (ind < len(s)) :
            encoded_string += s[ind]
            ind += 2*(numRows-1)

        # Middle Rows
        for i in range(1, numRows-1) :
            ind = i
            while (ind < len(s)) :
                encoded_string += s[ind]
                ind += 2*(numRows-i-1)
                
                if ind < len(s) :
                    encoded_string += s[ind]
                    ind += (2*i)
        
        # Last row
        ind = numRows - 1
        while (ind < len(s)) :
            encoded_string += s[ind]
            ind += 2*(numRows-1)

        return encoded_string
