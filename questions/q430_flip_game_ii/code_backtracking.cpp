class Solution {
    public:
        string s;
        bool canWin(string currentState) {
            s = currentState;
            return canWin();
        }
    
        bool canWin() {
            for (int i=0; i<s.length()-1; i++) {
                if (s[i] == '+' && s[i+1] == '+') {
                    s[i] = '-';
                    s[i+1] = '-';
                    bool oppResult = !canWin();
                    s[i] = '+';
                    s[i+1] = '+';
                    if (oppResult) {
                        return true;
                    }
                }
            }
            return false;
        }
    };
