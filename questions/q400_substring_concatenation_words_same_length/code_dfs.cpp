// This is not a efficient solution as it caused time limit exceeded in Leetcode


class Solution {
    public:
        bool traverse(int curSIndex, int curWordIndex, vector<vector<int>>& startWords, int wordLen, vector<bool>& hasVisited, int numVisited, int totalWordCount) {
            // We either exceed the size of s or if the current index has no words
            if (curSIndex>=startWords.size() || startWords[curSIndex].size() == 0 || hasVisited[curWordIndex]) {
                return false;
            }
    
            hasVisited[curWordIndex] = true;
            numVisited++;
    
            if (numVisited == totalWordCount) {
                return true;
            }
    
            if (curSIndex+wordLen < startWords.size()) {
                for (int i: startWords[curSIndex+wordLen]) {
                    if (!hasVisited[i]) {
                        if(traverse(curSIndex+wordLen, i, startWords, wordLen, hasVisited, numVisited, totalWordCount)) {
                            return true;
                        }
                    }
                }
            } 
    
            return false;
        }
    
        vector<int> findSubstring(string s, vector<string>& words) {
            int l=words[0].length();
            int n = words.size();
            int sl = s.length();
    
            vector<vector<int>> startWords(sl);
    
            int i=0,j=0;
            for (i=0; i<n; i++) {
                j = 0;
                while (j<sl) {
                    if (s.compare(j, l, words[i]) == 0) {
                        startWords[j].push_back(i);
                    }
                    j++;
                }
            }
    
            vector<int> ans;
            for (i=0; i<sl; i++) {
                if (startWords[i].size() > 0) {
                    vector<bool> hasVisited(n, false);
                    int numVisited=0;
                    for (int wordInd: startWords[i]) {
                        if (traverse(i, wordInd, startWords, l, hasVisited, numVisited, n)) {
                            ans.push_back(i);
                            break;
                        }
                    }
                }
            }
    
            return ans;
        }
};
