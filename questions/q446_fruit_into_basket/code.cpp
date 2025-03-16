class Solution {
    public:
        int totalFruit(vector<int>& fruits) {
            map<int, int> basket;
            int numTypes = 0;
            int maxTreeCount=0;
            int s=0,e=0;
            
            while (e < fruits.size()) {
                basket[fruits[e]]++;
                if (basket[fruits[e]] == 1) {
                    numTypes++;
                }
                
                while (numTypes > 2) {
                    basket[fruits[s]] --;
                    if (basket[fruits[s]] == 0) {
                        numTypes --;
                    }
                    s++;
                }
                e++;
                maxTreeCount = max(maxTreeCount, (e-s));
            }
            
            return maxTreeCount;
        }
    };
