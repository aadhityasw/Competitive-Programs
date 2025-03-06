// Uses a min heap

class NumberContainers {
    public:
        map<int, priority_queue<int, vector<int>, greater<int>>> numToInds;
        map<int, int> indToNum;
    
        NumberContainers() {
            
        }
        
        void change(int index, int number) {
            indToNum[index] = number;
            numToInds[number].push(index);
        }
        
        int find(int number) {
            if (numToInds.find(number) == numToInds.end() || numToInds[number].size() == 0) {
                return -1;
            }
            
            while (numToInds[number].size() > 0) {
                int curInd = numToInds[number].top();
                if (indToNum[curInd] != number) {
                    numToInds[number].pop();
                }
                else {
                    return curInd;
                }
            }
            return -1;
        }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
