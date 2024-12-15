class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (gas.size() == 1) {
            if (gas[0] >= cost[0]) {
                return 0;
            }
            return -1;
        }

        int i=1, cur_gas=(gas[0]-cost[0]), start=0;
        while (i!= start) {
            if (cur_gas >= 0) {
                cur_gas += (gas[i] - cost[i]);
                i++;
                if (i >= gas.size()) {
                    i = 0;
                }
            }
            else {
                start --;
                if (start == -1) {
                    start = gas.size()-1;
                }
                cur_gas += (gas[start] - cost[start]);
            }
        }

        if (cur_gas >= 0) {
            return i;
        }
        return -1;
    }
};