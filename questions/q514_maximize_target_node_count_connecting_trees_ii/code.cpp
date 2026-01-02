class Solution {
public:

    vector<vector<int>> constructGraph(vector<vector<int>>& edges) {
        vector<vector<int>> graph(edges.size()+1);
        for (int i=0; i<edges.size(); i++) {
            graph[edges[i][0]].push_back(edges[i][1]);
            graph[edges[i][1]].push_back(edges[i][0]);
        }

        return graph;
    }

    void findOddEvenCountFromNode(int curNode, int parNode, vector<vector<int>>& graph, int& nOdd, int& nEven, bool isEven) {
        if (isEven) {
            nEven++;
        }
        else {
            nOdd++;
        }

        for (int nextNode : graph[curNode]) {
            if (nextNode != parNode) {
                findOddEvenCountFromNode(nextNode, curNode, graph, nOdd, nEven, !isEven);
            }
        }
    }

    void propagateOddEvenCountsFromNode(int curNode, int parNode, vector<vector<int>>& graph, int nOdd, int nEven, vector<pair<int, int>>& oddEvenCountStore) {
        oddEvenCountStore[curNode] = {nOdd, nEven};

        for (int nextNode : graph[curNode]) {
            if (nextNode != parNode) {
                propagateOddEvenCountsFromNode(nextNode, curNode, graph, nEven, nOdd, oddEvenCountStore);
            }
        }
    }

    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        int n=edges1.size()+1, m=edges2.size()+1;
        vector<vector<int>> graph1 = constructGraph(edges1);
        vector<vector<int>> graph2 = constructGraph(edges2);

        int nOdd1=0, nOdd2=0, nEven1=0, nEven2=0;
        findOddEvenCountFromNode(0, -1, graph1, nOdd1, nEven1, true);
        findOddEvenCountFromNode(0, -1, graph2, nOdd2, nEven2, true);

        vector<pair<int, int>> oddEvenCountStore1(n);
        propagateOddEvenCountsFromNode(0, -1, graph1, nOdd1, nEven1, oddEvenCountStore1);

        vector<int> ans(n, 0);
        int numMaxEven2 = max(nOdd2, nEven2);
        for (int i=0; i<n; i++) {
            ans[i] = numMaxEven2 + oddEvenCountStore1[i].second;
        }

        return ans;
    }
};
