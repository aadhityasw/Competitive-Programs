class Solution {
    public:
        vector<string> ans;
    
        void combo(int n, string s, int numOpen) {
            if (n == 0) {
                while (numOpen > 0) {
                    s = s + ')';
                    numOpen--;
                }
                ans.push_back(s);
                return;
            }
    
            vector<char> para = {'(', ')'};
            combo(n-1, s+para[0], numOpen+1);
            if (numOpen > 0) {
                combo(n, s+')', numOpen-1);
            }
        }
    
        vector<string> generateParenthesis(int n) {
            combo(n-1, "(", 1);
            return ans;
        }
    };
