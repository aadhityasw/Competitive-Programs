class Solution {
    public:
        int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
            priority_queue<int, vector<int>, greater<int>> pHeap;
            for (int p : players) {
                pHeap.push(p);
            }
    
            priority_queue<int, vector<int>, greater<int>> tHeap;
            for (int t : trainers) {
                tHeap.push(t);
            }
    
            int matchCount=0;
            while (pHeap.size()>0 && tHeap.size()>0) {
                if (pHeap.top() > tHeap.top()) {
                    tHeap.pop();
                }
                else {
                    matchCount++;
                    tHeap.pop();
                    pHeap.pop();
                }
            }
    
            return matchCount;
        }
    };
