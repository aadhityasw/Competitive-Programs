
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
    public:
        map<Node*, Node*> oldToNewNode;
    
        Node* cloneGraph(Node* node) {
    
            if (node == nullptr) {
                return nullptr;
            }
    
            // We have processed this node already
            if (oldToNewNode.find(node) != oldToNewNode.end()) {
                return oldToNewNode[node];
            }
    
            Node *newNode = new Node(node->val);
            oldToNewNode[node] = newNode;
            for (Node *ptr : node->neighbors) {
                if (oldToNewNode.find(ptr) != oldToNewNode.end()) {
                    newNode->neighbors.push_back(oldToNewNode[ptr]);
                }
                else {
                    newNode->neighbors.push_back(cloneGraph(ptr));
                }
            }
    
            return newNode;
        }
    };
