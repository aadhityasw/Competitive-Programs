class Solution {
    public:
        void dfs_search(int i, map<int, vector<int>> &adj, set<int> &curPath, vector<bool> &visited, vector<int> &schedule, bool &isPossible) {
            if (visited[i] || !isPossible) {
                return;
            }
    
            curPath.insert(i);
            for (int o: adj[i]) {
                if (curPath.count(o) > 0) {
                    isPossible = false;
                    return;
                }
                else if (!visited[o]) {
                    dfs_search(o, adj, curPath, visited, schedule, isPossible);
                }
    
                if (!isPossible) {
                    return;
                }
            }
    
            visited[i] = true;
            curPath.erase(i);
            schedule.push_back(i);
        }
    
        vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
            map<int, vector<int>> outBoundEdges;
    
            for (const auto &ele : prerequisites) {
                outBoundEdges[ele[0]].push_back(ele[1]);
            }
    
            vector<bool> visited(numCourses, false);
            vector<int> schedule;
            bool isPossible = true;
            for (int i=0; i<numCourses; i++) {
                if (!visited[i]) {
                    set<int> curPath;
                    dfs_search(i, outBoundEdges, curPath, visited, schedule, isPossible);
                }
            }
    
            if (isPossible) {
                return schedule;
            }
            schedule.erase(schedule.begin(), schedule.end());
            return schedule;
        }
    };
