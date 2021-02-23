class Solution:
    def longest_word_finder(self, a, b, s, word) :
        while a >= 0 and b < len(s) and s[a] == s[b] :
            word = s[a] + word + s[b]
            a -= 1
            b += 1
        return word

    def longestPalindrome(self, s: str) -> str :
        max_length_string = ""
        for i in range(len(s)) :
            # For even length palindrome
            word1 = self.longest_word_finder(i - 1, i, s, "")
            # For odd length palindrome
            word2 = self.longest_word_finder(i - 1, i + 1, s, str(s[i]))

            if len(word1) > len(max_length_string) :
                max_length_string = word1
            if len(word2) > len(max_length_string) :
                max_length_string = word2

        return max_length_string
