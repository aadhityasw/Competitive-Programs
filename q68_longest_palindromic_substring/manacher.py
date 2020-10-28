class Solution:
    """
    Uses Manacher's Algorithm to solve this in linear time.

    When we find a palindrome, we check for these 4 conditions from the next position till the next right edge, to determine a candidate who can possibly hava a longer palindromic substring.
    We append a `$` sign before and after every character so as to consider the cases of even length palindromes. So by this the actual length of the palindrome will be half of the one calculated by this method.

    The cases are :
    (i) The palindrome in the right node is totally contained inside the current palindrome, and so in this case it cannot reach outside and thus this cannot be our next candidate.
    (ii) If the current palindrome spans till the end of the entire string, we exit the process, as there is no point in moving forwward.
    (iii) If the right palindrome extends exactly until the edge of the current palindrome (by looking at the minimum of its mirror in the left side of the current index and its distance form the end of current palindrome), and its left side mirror also extends only until the left end of the current palindrome. So this can extend further, and we consider this index to be a candidate for our next center.
    (iv) If in case we get an index which extends exactly till the right side, but its mirror extends outside the left end of the current palindrome, then we do not consider this to be a candidate.
    """
    def longestPalindrome(self, s: str) -> str :
        # Modify the string for generalizing the process for even length palindrome
        word = "$"
        for ch in s :
            word = word + ch + "$"

        # To store the length of the palindrome with a particular index as the center
        lengths = [0] * len(word)
        start = 0
        end = 0
        i = 0
        maximum_substring = ""

        while i < len(word) :
            # Finds the length of the palindrome with ith index as the center
            while start > 0 and end < (len(word)-1) and word[start-1] == word[end+1] :
                start -= 1
                end += 1
            lengths[i] = end - start + 1

            # Update the storage for the maximum length substring
            if lengths[i]//2 > len(maximum_substring) :
                maximum_substring = ""
                for ch in word[start:end+1] :
                    if ch != '$' :
                        maximum_substring += ch

            # When a palindrome reached the end of the string, there is no point in moving forward with the search.
            if end == (len(word) - 1) :
                break

            # Decide on a candidate for the next center as outside of the current palindrome
            if i % 2 == 0 :
                nextCenter = end + 1
            else :
                nextCenter = end
            
            # Select a candidate for the next center
            for j in range(i+1, end+1) :
                # The jth index will host a palindrome of length equal to its left mirror by `i`.
                # Or if the left mirror's palindrome extends beyond the left end of the current palindrome, we cannot say the same for the right mirror, 
                #   so in this case we cansider it to host until the right end of the current palindrome because if the right mirror's palindrome had extended beyond the right edge as the left one, then the current palindrome would have been longer.
                lengths[j] = min(lengths[i- (j-i)], 2*(end - j) + 1)

                # So if the right and the left mirrors extends exactly till the left and the right end ofthe current palindrome respectively, then we consider it to be a solution
                if (j + lengths[i - (j - i)]//2) == end :
                    nextCenter = j
                    break

            # Updating the parameters for the next center
            i = nextCenter
            end = i + lengths[i] // 2
            start = i - lengths[i] // 2

        return maximum_substring
