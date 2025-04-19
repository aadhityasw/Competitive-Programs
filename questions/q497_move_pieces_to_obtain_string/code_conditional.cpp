class Solution {
	public:

	vector<int> getPiecePositions(char piece, string s) {
		// Get the size of the string
        int n = s.length();

        // Initialize vector to store the positions
        vector<int> positions;

            for (int i=0; i<n; i++) {
                if (s[i] == piece) {
                    positions.push_back(i);
			}
        } 

        return positions;
	}

	int searchForPosFromOtherPiece(int ele, vector<int>& arr) {
		// Get the number of elements in arr
		int n = arr.size();

		// Use binary search to find the position
		int low = 0;
		int high = n-1;
		while (low < high) {
			int mid = low + (high-low)/2;
			if (ele <= arr[mid]) {
				high = mid;
			}
			else {
				low = mid+1;
			}
		}

		if (low < arr.size() && ele > arr[low]) {
            return low+1;
        }
        return low;
	}

	bool canChange(string start, string target) {
		// Get the length of the game board
		int n = start.length();

		// Process the boards to store the positions of the pieces
		vector<int> startLPos = getPiecePositions('L', start);
		vector<int> startRPos = getPiecePositions('R', start);
		vector<int> targetLPos = getPiecePositions('L', target);
		vector<int> targetRPos = getPiecePositions('R', target);

		// Condition 1: Make sure that the number of pieces are the same
		if (startLPos.size() != targetLPos.size() || startRPos.size() != targetRPos.size()) {
			return false;
		}

		// Condition 2: Make sure every left piece has moved only left and the right piece has moved only right
		for (int i=0; i<startLPos.size(); i++) {
			if (startLPos[i] < targetLPos[i]) {
				// ith L piece has moved right
				return false;
			}
		}
		for (int i=0; i<startRPos.size(); i++) {
			if (startRPos[i] > targetRPos[i]) {
				// ith R piece has moved left
				return false;
			}
		}

		// Condition 3 : While moving the left and right pieces, we do not encounter any piece of the other type in the middle
		for (int i=0; i<startLPos.size(); i++) {
			int startPos = searchForPosFromOtherPiece(startLPos[i], startRPos);
			int targetPos = searchForPosFromOtherPiece(targetLPos[i], startRPos);
			
			if (startPos > targetPos) {
				// There is a R between the source and target L
				return false;
			}

            if (startPos < startRPos.size() && targetLPos[i] == startRPos[startPos]) {
				return false;
			}
		}

        for (int i=0; i<startLPos.size(); i++) {
			int startPos = searchForPosFromOtherPiece(startLPos[i], targetRPos);
			int targetPos = searchForPosFromOtherPiece(targetLPos[i], targetRPos);
			
			if (startPos > targetPos) {
				// There is a R between the source and target L
				return false;
			}

            if (startPos < targetRPos.size() && targetLPos[i] == targetRPos[startPos]) {
				return false;
			}
		}

		for (int i=0; i<startRPos.size(); i++) {
			int startPos = searchForPosFromOtherPiece(startRPos[i], startLPos);
			int targetPos = searchForPosFromOtherPiece(targetRPos[i], startLPos);
			
			if (startPos < targetPos) {
				// There is a L between the source and target R 
				return false;
			}

            if (startPos < startLPos.size() && targetRPos[i] == startLPos[startPos]) {
				return false;
			}
		}

        for (int i=0; i<startRPos.size(); i++) {
			int startPos = searchForPosFromOtherPiece(startRPos[i], targetLPos);
			int targetPos = searchForPosFromOtherPiece(targetRPos[i], targetLPos);
			
			if (startPos < targetPos) {
				// There is a L between the source and target R 
				return false;
			}

            if (startPos < targetLPos.size() && targetRPos[i] == targetLPos[startPos]) {
				return false;
			}
		}

		// If we have satisfied all conditions
		return true;
	}
};
