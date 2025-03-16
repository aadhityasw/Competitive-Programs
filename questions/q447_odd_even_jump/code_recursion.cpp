class Solution {
    public:
        map<int, bool> oddStepRechable;
        map<int, bool> evenStepRechable;
        
        bool takeEvenStep(int pos, vector<int>& arr) {
            if (pos == arr.size()-1) {
                return true;
            }
            
            if (evenStepRechable.find(pos) != evenStepRechable.end()) {
                return evenStepRechable[pos];
            }
            
            int nextPos=-1;
            for (int i=pos+1; i<arr.size(); i++) {
                if (arr[i] <= arr[pos]) {
                    if (nextPos == -1 || arr[nextPos] < arr[i]) {
                        nextPos = i;
                    }
                }
            }
            
            if (nextPos == -1) {
                evenStepRechable[pos] = false;
            }
            else {
                evenStepRechable[pos] = takeOddStep(nextPos, arr);
            }
            
            return evenStepRechable[pos];
        }
        
        bool takeOddStep(int pos, vector<int>& arr) {
            if (pos == arr.size()-1) {
                return true;
            }
            
            if (oddStepRechable.find(pos) != oddStepRechable.end()) {
                return oddStepRechable[pos];
            }
            
            int nextPos=-1;
            for (int i=pos+1; i<arr.size(); i++) {
                if (arr[i] >= arr[pos]) {
                    if (nextPos == -1 || arr[nextPos] > arr[i]) {
                        nextPos = i;
                    }
                }
            }
            
            if (nextPos == -1) {
                oddStepRechable[pos] = false;
            }
            else {
                oddStepRechable[pos] = takeEvenStep(nextPos, arr);
            }
            
            return oddStepRechable[pos];
        }
        
        int oddEvenJumps(vector<int>& arr) {
            int totalCount=0;
            
            for (int i=0; i<arr.size(); i++) {
                if (takeOddStep(i, arr)) {
                    totalCount ++;
                }
            }
            
            return totalCount;
        }
    };
