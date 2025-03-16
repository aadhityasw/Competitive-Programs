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
        ListNode *detectCycle(ListNode *head) {
            ListNode* fastPtr = head;
            ListNode* slowPtr = head;
    
            while (fastPtr && fastPtr->next) {
                fastPtr = fastPtr->next->next;
                slowPtr = slowPtr->next;
                if (fastPtr == slowPtr) {
                    break;
                }
            }
    
            if (!fastPtr || !fastPtr->next) {
                return nullptr;
            }
    
            ListNode* ptr = head;
            while (ptr != slowPtr) {
                ptr = ptr->next;
                slowPtr = slowPtr->next;
            }
            return ptr;
        }
    };
