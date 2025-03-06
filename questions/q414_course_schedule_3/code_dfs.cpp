// Causes time limit exceeded in leetcode


class Solution {
    public:
        int maxCount = 0;
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> deadlineHeap;
    
        void search(int curTime, int curCount) {
            stack<vector<int>> searchStack;
    
            maxCount = max(maxCount, curCount);
    
            while (deadlineHeap.size() > 0) {
                int nextDeadline = deadlineHeap.top()[0];
                int nextCourseTime = deadlineHeap.top()[1];
                searchStack.push(deadlineHeap.top());
                deadlineHeap.pop();
                if (curTime + nextCourseTime <= nextDeadline) {
                    search(curTime + nextCourseTime, curCount+1);
                }
            }
    
            while (searchStack.size() > 0) {
                deadlineHeap.push(searchStack.top());
                searchStack.pop();
            }
        }
    
        int scheduleCourse(vector<vector<int>>& courses) {
            
            for (const auto &c : courses) {
                deadlineHeap.push({c[1], c[0]});
            }
    
            maxCount = 0;
            search(0, 0);
            return maxCount;
        }
    };
