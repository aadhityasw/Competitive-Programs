// We do a DFS, but this does not pass all test cases in leetcode and causes time limit exceeded

class Node {
    public:
    int value;
    vector<Node*> nextCourses;

    Node() {
        value = 0;
    }

    Node(int v) {
        value = v;
    }
};

class Solution {
public:
    bool validateNonCyclicGraph(Node* ptr, set<Node*> visited) {
        if (visited.find(ptr) != visited.end()) {
            return false;
        }

        visited.insert(ptr);
        for (const auto& ele : ptr->nextCourses) {
            if (!validateNonCyclicGraph(ele, visited)) {
                return false;
            }
        }

        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<Node*> valToNode(numCourses, nullptr);

        // Construct the graph
        for (int i = 0; i<prerequisites.size(); i++) {
            Node* src;
            Node* dest;
            if (valToNode[prerequisites[i][0]] == nullptr) {
                src = new Node(prerequisites[i][0]);
                valToNode[prerequisites[i][0]] = src;
            }
            else {
                src = valToNode[prerequisites[i][0]];
            }

            if (valToNode[prerequisites[i][1]] == nullptr) {
                dest = new Node(prerequisites[i][1]);
                valToNode[prerequisites[i][1]] = dest;
            }
            else {
                dest = valToNode[prerequisites[i][1]];
            }

            src->nextCourses.push_back(dest);
        }

        // Traverse the graph
        set<Node*> visited;
        for (const auto &ele : valToNode) {
            if (ele != nullptr && !validateNonCyclicGraph(ele, visited)) {
                return false;
            }
        }

        return true;
    }
};
