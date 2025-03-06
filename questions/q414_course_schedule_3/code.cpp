class Solution {
    public:
        int scheduleCourse(vector<vector<int>>& courses) {
            vector<vector<int>> deadlines;
            for (const auto &ele : courses) {
                deadlines.push_back({ele[1], ele[0]});
            }
            sort(deadlines.begin(), deadlines.end());
    
            priority_queue<int> takenCourseDuration;
            int curTime = 0;
            int numCourses = 0;
            for (int i = 0; i<deadlines.size(); i++) {
                if (curTime + deadlines[i][1] > deadlines[i][0]) {
                    if (takenCourseDuration.size() > 0 && takenCourseDuration.top() > deadlines[i][1]) {
                        if (curTime - takenCourseDuration.top() + deadlines[i][1] <= deadlines[i][0]) {
                            curTime = curTime - takenCourseDuration.top() + deadlines[i][1];
                            takenCourseDuration.pop();
                            takenCourseDuration.push(deadlines[i][1]);
                        }
                    }
                }
                else {
                    curTime += deadlines[i][1];
                    numCourses ++;
                    takenCourseDuration.push(deadlines[i][1]);
                }
            }
    
            return numCourses;
        }
    };
