// This is the leetcode version of the problem


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    public:
        bool hasCycle(ListNode *head) {
            ListNode* slowPtr=head;
            ListNode* fastPtr=head;
    
            do {
                if (fastPtr == nullptr) {
                    return false;
                }
                fastPtr = fastPtr->next;
                slowPtr = slowPtr->next;
                if (fastPtr == nullptr) {
                    return false;
                }
                fastPtr = fastPtr->next;
    
                if (fastPtr == slowPtr) {
                    return true;
                }
            } while (slowPtr && fastPtr && slowPtr != fastPtr);
    
            return slowPtr == fastPtr;
        }
    };
