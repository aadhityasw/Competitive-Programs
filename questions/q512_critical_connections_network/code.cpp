class Solution {
public:

    int timer;

    Solution() {
        timer = 0;
    }

    vector<vector<int>> formGraph(int n, vector<vector<int>>& connections) {
        vector<vector<int>> graph(n);

        for (int i=0; i<connections.size(); i++) {
            graph[connections[i][0]].push_back(connections[i][1]);
            graph[connections[i][1]].push_back(connections[i][0]);
        }

        return graph;
    }

    void traverseDFS(int curNode, int parNode, vector<bool>& visited, vector<int>& timeInserted, vector<int>& minTime, vector<vector<int>>& graph, vector<vector<int>>& bridges) {

        visited[curNode] = true;
        timeInserted[curNode] = timer;
        minTime[curNode] = timer;
        timer++;

        for (int adjNode : graph[curNode]) {
            if (adjNode == parNode) {
                continue;
            }

            if(!visited[adjNode]) {
                traverseDFS(adjNode, curNode, visited, timeInserted, minTime, graph, bridges);

                minTime[curNode] = min(minTime[curNode], minTime[adjNode]);
                if (timeInserted[curNode] < minTime[adjNode]) {
                    bridges.push_back({curNode, adjNode});
                }
            }
            else {
                minTime[curNode] = min(minTime[curNode], minTime[adjNode]);
            }
        }
    }

    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<int>> graph = formGraph(n, connections);

        vector<bool> visited(n, false);
        vector<int> timeInserted(n, 0);
        vector<int> minTime(n, 0);
        vector<vector<int>> bridges;

        traverseDFS(0, -1, visited, timeInserted, minTime, graph, bridges);

        return bridges;
    }
};
