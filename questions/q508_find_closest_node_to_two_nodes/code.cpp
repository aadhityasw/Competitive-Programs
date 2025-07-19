class Solution {
public:

    vector<int> getDistanceFromNode(vector<int>& edges, int sNode) {
        int n = edges.size();
        vector<bool> visited(n, false);
        vector<int> distance(n, INT_MAX);

        int ptr = sNode;
        int curDist = 0;
        while (ptr>=0 && !visited[ptr]) {
            distance[ptr] = curDist++;
            visited[ptr] = true;
            ptr = edges[ptr];
        }

        return distance;
    }

    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        
        int n = edges.size();

        // Get the distance of all the nodes from the source node
        vector<int> distance1 = getDistanceFromNode(edges, node1);
        vector<int> distance2 = getDistanceFromNode(edges, node2);

        // Find the min - maximum distance of each node from node1 and node2
        int minNode = -1;
        int minDist = INT_MAX;
        for (int i=0; i<n; i++) {
            int curDist = max(distance1[i], distance2[i]);
            if (minDist > curDist) {
                minNode = i;
                minDist = curDist;
            }
        }

        return minNode;
    }
};
