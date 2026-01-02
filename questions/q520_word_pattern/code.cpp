class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> charToWord;
        unordered_map<string, char> wordToChar;

        int chInd=0;
        s = s + ' ';
        int n = s.length();
        string curWord = "";

        int i=0;
        while (i < n) {
            if (chInd >= pattern.length()) {
                return false;
            }

            if (s[i] == ' ') {
                if (charToWord.find(pattern[chInd]) == charToWord.end() && wordToChar.find(curWord) == wordToChar.end()) {
                    charToWord[pattern[chInd]] = curWord;
                    wordToChar[curWord] = pattern[chInd];
                }
                else if (charToWord.find(pattern[chInd]) == charToWord.end() || wordToChar.find(curWord) == wordToChar.end()) {
                    return false;
                }
                else if (charToWord[pattern[chInd]] != curWord || wordToChar[curWord] != pattern[chInd]) {
                    return false;
                }
                curWord = "";
                chInd++;
            }
            else {
                curWord += s[i];
            }

            i++;
        }

        if (chInd != pattern.length()) {
            return false;
        }

        return true;
    }
};
