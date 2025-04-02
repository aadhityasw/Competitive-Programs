class Solution {
    public:
        string reorganizeString(string s) {
            int n = s.length();
    
            // Store the frequency
            vector<int> freq(26);
            for (char c : s) {
                freq[(int)c - 97]++;
            }
    
            // Create a max-heap with (freq, char)
            priority_queue<pair<int, char>> freqHeap;
            for (int i=0; i<26; i++) {
                if (freq[i] > 0) {
                    pair<int, char> p = {freq[i], (char)(i+97)};
                    freqHeap.push(p);
                }
            }
    
            // Fill in the new string based on this heap
            string ans;
            while (!freqHeap.empty()) {
                pair<int, char> p1 = freqHeap.top();
                freqHeap.pop();
                if (ans.length()== 0 || ans[ans.length()-1]!=p1.second) {
                    ans.push_back(p1.second);
                    p1.first--;
                }
                else {
                    if (freqHeap.empty()) {
                        return "";
                    }
                    pair<int, char> p2 = freqHeap.top();
                    freqHeap.pop();
                    ans.push_back(p2.second);
                    p2.first--;
                    if (p2.first > 0) {
                        freqHeap.push(p2);
                    }
                }
                if (p1.first > 0) {
                    freqHeap.push(p1);
                }
            }
    
            return ans;
        }
    };
