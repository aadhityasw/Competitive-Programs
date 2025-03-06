// Uses a stack
// Causes Time limit exceeded in some testcases in leetcode, but is a valid solution

class NumberContainers {
    public:
        map<int, set<int>> store;
        map<int, int> indToNum;
    
        NumberContainers() {
            
        }
        
        void change(int index, int number) {
            if (indToNum.find(index) != indToNum.end()) {
                store[indToNum[index]].erase(index);
            }
            indToNum[index] = number;
            store[number].insert(index);
        }
        
        int find(int number) {
            if (store.find(number) == store.end() || store[number].size() == 0) {
                return -1;
            }
            return *store[number].begin();
        }
    };
    
/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
