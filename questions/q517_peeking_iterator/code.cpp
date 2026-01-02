/*
 * Below is the interface for Iterator, which is already defined for you.
 * **DO NOT** modify the interface for Iterator.
 *
 *  class Iterator {
 *		struct Data;
 * 		Data* data;
 *  public:
 *		Iterator(const vector<int>& nums);
 * 		Iterator(const Iterator& iter);
 *
 * 		// Returns the next element in the iteration.
 *		int next();
 *
 *		// Returns true if the iteration has more elements.
 *		bool hasNext() const;
 *	};
 */

class PeekingIterator : public Iterator {
public:

    bool hasPeeked, hasNextWhenPeeked;
    int peekedVal;

	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    hasPeeked = false;
        hasNextWhenPeeked = false;
        peekedVal = -1;
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	int peek() {

        if (!hasPeeked) {
            hasNextWhenPeeked = Iterator::hasNext();
            peekedVal = Iterator::next();
            hasPeeked = true;
        }
        
        return peekedVal;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    if (hasPeeked) {
            hasPeeked = false;
            return peekedVal;
        }
        else {
            return Iterator::next();
        }
	}
	
	bool hasNext() const {
	    if (hasPeeked) {
            return hasNextWhenPeeked;
        }
        else {
            return Iterator::hasNext();
        }
	}
};
