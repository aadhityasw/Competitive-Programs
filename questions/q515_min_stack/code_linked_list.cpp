class Node {
    public:

    Node *left, *right, *minNode;
    int data;

    Node (int d) {
        left = nullptr;
        right = nullptr;
        minNode = this;
        data = d;
    }
};

class MinStack {
public:

    Node *head;

    MinStack() {
        head = nullptr;
    }
    
    void push(int val) {
        Node* ptr = new Node(val);
        if (head == nullptr) {
            head = ptr;
            ptr->minNode = ptr;
        }
        else {
            ptr->right = head;
            head->left = ptr;
            ptr->minNode = (ptr->data < head->minNode->data)? ptr : head->minNode;
            head = ptr;
        }
    }
    
    void pop() {
        Node* ptr = head->right;
        head->right = nullptr;
        head->minNode = nullptr;
        delete(head);
        head = ptr;
        if (head != nullptr) {
            head->left = nullptr;
        }
    }
    
    int top() {
        return head->data;
    }
    
    int getMin() {
        return head->minNode->data;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
