/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *ptr1, *ptr2;
        ptr1 = head;
        ptr2 = head;
        int numShift = 0;

        while (ptr1->next != nullptr) {

            ptr1 = ptr1->next;
            if (ptr1->next == nullptr) {
                numShift = n-1;
            }
            else {
                numShift = n;
            }

            // Shift the lead pointer by n times in normal case
            // And n-1 times in the last case (Just so as to remove the next node after this is done)
            while (numShift > 0) {
                numShift --;
                if (ptr2->next == nullptr) {
                    // Go from last node to first
                    ptr2 = head;
                }
                else {
                    ptr2 = ptr2->next;
                }
            }
        }

        if (ptr2->next == nullptr) {
            // Removing first node
            ptr1 = head;
            head = head->next;
            ptr1->next = nullptr;
        }
        else if (ptr2->next->next == nullptr) {
            // Removing last node
            ptr2->next = nullptr;
        }
        else {
            // Removing a middle node
            ptr1 = ptr2->next;
            ptr2->next = ptr1->next;
            ptr1->next = nullptr;
        }

        return head;
    }
};
