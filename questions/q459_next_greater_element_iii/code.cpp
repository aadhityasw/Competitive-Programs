class Solution {
    public:
        int nextGreaterElement(int n) {
            string numS = to_string(n);
            int numDigits = numS.length();
    
            int pos=-1;
            for (int i=numDigits-2; i>=0; i--) {
                if (numS[i]<numS[i+1]) {
                    pos = i;
                    break;
                }
            }
    
            if (pos == -1) {
                return -1;
            }
    
            // Take the first pos characters as they need to be untouched
            string untouchedPrefix = numS.substr(0, pos);
            // Take the last (numDigits-pos) digits to be the postfix, this should be processed further
            string postfix = numS.substr(pos+1);
    
            // Find the first digit that is greater than numS[pos], and put it there
            int pos2=-1;
            for (int i=postfix.size()-1; i>=0; i--) {
                if (postfix[i] > numS[pos]) {
                    pos2 = i;
                    break;
                }
            }
    
            string nextGreaterNum = untouchedPrefix + postfix[pos2];
            postfix[pos2] = numS[pos];
            reverse(postfix.begin(), postfix.end());
            nextGreaterNum = nextGreaterNum + postfix;
    
            string maxcap = to_string(INT_MAX);
            if (nextGreaterNum.length() < maxcap.length() || (nextGreaterNum.length() == maxcap.length() &&  nextGreaterNum.compare(maxcap) <= 0)) {
                return stoi(nextGreaterNum);
            }
            return -1;
        }
    };
