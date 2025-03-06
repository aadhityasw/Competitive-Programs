// For the Leetcode Problem

// Leetcode 207


class Solution {
    public:
        bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
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
            int numVisited = 0;
            while (frontier.size() > 0) {
                int outEdge = frontier.front();
                frontier.pop();
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
    
            return numVisited == numCourses;
        }
    };
