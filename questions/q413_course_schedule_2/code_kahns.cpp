class Solution {
    public:
        vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
            map<int, queue<int>> outBoundEdges;
            map<int, set<int>> inBoundEdges;
    
            for (const auto &ele : prerequisites) {
                inBoundEdges[ele[1]].insert(ele[0]);
                outBoundEdges[ele[0]].push(ele[1]);
            }
    
            queue<int> frontier;
            for (int i=0; i<numCourses; i++) {
                if (inBoundEdges[i].size() == 0) {
                    frontier.push(i);
                }
            }
    
            vector<bool> visited(numCourses, false);
            vector<int> schedule;
            int numVisited = 0;
            while (frontier.size() > 0) {
                int outEdge = frontier.front();
                frontier.pop();
                schedule.push_back(outEdge);
                while (outBoundEdges[outEdge].size() > 0) {
                    int inEdge = outBoundEdges[outEdge].front();
                    outBoundEdges[outEdge].pop();
                    inBoundEdges[inEdge].erase(outEdge);
                    if (inBoundEdges[inEdge].size() == 0 && !visited[inEdge]) {
                        frontier.push(inEdge);
                    }
                }
                numVisited++;
                visited[outEdge] = true;
            }
    
            if (numVisited == numCourses) {
                reverse(schedule.begin(), schedule.end());
                return schedule;
            }
            schedule.erase(schedule.begin(), schedule.end());
            return schedule;
        }
    };
