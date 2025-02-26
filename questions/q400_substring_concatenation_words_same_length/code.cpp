class Solution {
    public:
        vector<int> findSubstring(string s, vector<string>& words) {
            int sl = s.length();
            int n = words.size();
            int l = words[0].length();
    
            map<string, int> wordsMap;
            for (string word: words) {
                wordsMap[word]++;
            }
    
            set<int> ansSet;
    
            for (int i=0; i<l; i++) {
                int startIndex = i;
                int endIndex = i;
                string curWord;
                map<string, int> seen;
                int numSeen=0;
    
                while (endIndex <= sl-l) {
                    // Increase the window to the right
                    curWord = s.substr(endIndex, l);
                    if(wordsMap.find(curWord) != wordsMap.end()) {
                        seen[curWord] ++;
                        numSeen++;
                    }
                    else {
                        startIndex = endIndex+l;
                        endIndex+=l;
                        numSeen=0;
                        seen.clear();
                        continue;
                    }
                    endIndex+=l;
    
                    // Reduce the window from front if we have more than required of the current word
                    while (seen[curWord] > wordsMap[curWord]) {
                        seen[s.substr(startIndex, l)]--;
                        numSeen--;
                        startIndex += l;
                    }
                    
                    // Now if we have the exact match of words, we store this value
                    if (numSeen == n) {
                        ansSet.insert(startIndex);
                    }
                }
            }
    
            vector<int> ans(ansSet.begin(), ansSet.end());
            return ans;
        }
    };
