#include <vector>

class Node {
    

    public:
    int value, count;
    Node *left, *right;
    Node(int val) {
        this->value = val;
        this->count = 1;
        this->left = NULL;
        this->right = NULL;
    }

    void insert (int val) {
        if (this->value > val)
        {
            if (this->left == NULL)
            {
                this->left = new Node(val);
            }
            else
            {
                this->left->insert(val);
            }
        }
        else
        {
            if (this->right == NULL)
            {
                this->right = new Node(val);
            }
            else
            {
                this->right->insert(val);
            }
        }
    }

    int update(int more_count) {
        if (this->right != NULL) {
            this->count += this->right->update(more_count);
        }
        else {
            this->count += more_count;
        }
        int c = this->count;
        if (this->left != NULL) {
            c = this->left->update(this->count);
        }
        return c;
    }

    int search() {
        int max_val = 0;

        int cur = this->value;
        if (this->count < cur) {
            cur = this->count;
        }
        if (max_val < cur) {
            max_val = cur;
        }

        if (this->left != NULL) {
            int left = this->left->search();
            if (left > max_val) {
                max_val = left;
            }
        }
        if (this->right != NULL) {
            int right = this->right->search();
            if (right > max_val) {
                max_val = right;
            }
        }

        
        return max_val;
    }
};

class Solution {
public:
    int hIndex(vector<int>& citations) {
        Node* root = new Node(citations[0]);

        for (int i=1; i<citations.size(); i++) {
            root->insert(citations[i]);
        }
        root->update(0);

        return root->search();
    }
};