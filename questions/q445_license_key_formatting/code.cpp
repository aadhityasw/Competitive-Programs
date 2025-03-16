class Solution {
    public:
        string licenseKeyFormatting(string s, int k) {
            
            string ans = "";
            int curAreaLength=0;
            for (int i=s.length()-1; i>=0; i--) {
                if (s[i] == '-') {
                    continue;
                }
                char ch = s[i];
                if (ch >= 97) {ch -= 32;}
                if (curAreaLength == k) {
                    curAreaLength = 0;
                    ans.push_back('-');
                }
                ans.push_back(ch);
                curAreaLength ++;
            }
    
            reverse(ans.begin(), ans.end());
            return ans;
        }
    };
