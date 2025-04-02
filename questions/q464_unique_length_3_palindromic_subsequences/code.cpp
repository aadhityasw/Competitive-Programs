class Solution {
    public:
        int countPalindromicSubsequence(string s) {
            map<char, vector<int>> charPos;
            int n = s.length();
            
            for (int i=0; i<n; i++) {
                charPos[s[i]].push_back(i);
            }
    
            int numPalindrome=0;
            for (const auto& pair : charPos) {
                char ch = pair.first;
                if (charPos[ch].size()<=1) {
                    continue;
                }
                int fPos = charPos[ch][0];
                int lPos = charPos[ch][charPos[ch].size()-1];
                for (const auto& pair : charPos) {
                    char ch2 = pair.first;
                    for (int i=0; i<charPos[ch2].size(); i++) {
                        if (charPos[ch2][i]>fPos && charPos[ch2][i]<lPos) {
                            numPalindrome++;
                            break;
                        }
                    }
                }
            }
    
            return numPalindrome;
        }
    };
