// Leetcode Version


class Node {
    public :
    int key, value;
    Node *left, *right;

    Node() {
        key = 0;
        value = 0;
        left = nullptr;
        right = nullptr;
    }

    Node(int k, int v) {
        key = k;
        value = v;
        left = nullptr;
        right = nullptr;
    }
};

class LRUCache {
public:
    queue<int> cache;
    set<int> curKeys;
    map<int, Node*> store;
    int curCount, capacity;
    Node *start, *end;

    LRUCache(int cap) {
        capacity = cap;
        curCount = 0;
        start = nullptr;
    }

    void addNodeToEnd(Node* ptr) {
        if (start == nullptr) {
            start = ptr;
            end = ptr;
        }
        else {
            end->right = ptr;
            ptr->left = end;
            end = end->right;
        }
    }

    void removeAndReattachNode(Node* ptr) {
        if (ptr == start && ptr == end) {
            return;
        }
        else if (ptr == start) {
            start = start->right;
            start->left = nullptr;
            ptr->right = nullptr;
            end->right = ptr;
            ptr->left = end;
            end = end->right;
        }
        else if (ptr == end) {
            return;
        }
        else {
            Node* prev = ptr->left;
            Node* next = ptr->right;
            ptr->right = nullptr;
            ptr->left = end;
            end->right = ptr;
            end = end->right;
            prev->right = next;
            next->left = prev;
        }
    }
    
    int get(int key) {
        if (curKeys.count(key) > 0) {
            Node* ptr = store[key];
            removeAndReattachNode(ptr);

            return store[key]->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        Node *ptr;
        if (curKeys.count(key) > 0) {
            store[key]->value = value;
            ptr = store[key];

            removeAndReattachNode(ptr);
        }
        else {
            ptr = new Node(key, value);
            addNodeToEnd(ptr);
            curCount++;
            curKeys.insert(key);
            store[key] = ptr;

            if (curCount > capacity) {
                curKeys.erase(start->key);
                store[start->key] = nullptr;
                curCount--;

                ptr = start;
                start = start->right;
                start->left = nullptr;
                ptr->right = nullptr;
                ptr = nullptr;
            }
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
