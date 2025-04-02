// This is for the leetcode version of the problem


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
	void reorderList(ListNode* head) {
		// Find the length of the list and create the stack
		int listLength = 0;
		ListNode* ptr = head;
		stack<ListNode*> nodeStack;
		while (ptr != nullptr) {
			nodeStack.push(ptr);
			ptr = ptr->next;
			listLength++;
		}

		// Need to do this operation half the times as the length of list
		int numOperate = (listLength - 1) / 2;
		ptr = head;
		while (!nodeStack.empty() && numOperate > 0 && ptr != nullptr) {
			ListNode* nextPtr = nodeStack.top();
			nodeStack.pop();
			numOperate --;

			nextPtr->next = ptr->next;
			ptr->next = nextPtr;
			ptr = ptr->next->next;
		}

		if (ptr != nullptr && listLength % 2 == 0) {
			ptr = ptr->next;
		}

		if (ptr != nullptr) {
			ptr->next = nullptr;
		}
	}
};
