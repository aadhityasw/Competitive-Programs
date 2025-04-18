// This take the code of 3D and reduces 1 dimensions
// Because p3 is just p1+p2 at all times

class Solution {
	public:

	vector<vector<bool>> dp;
	vector<vector<bool>> visited;

	bool checkInterleaving(int p1, int p2, string s1, string s2, string s3) {
		
		// Check if the positions is still under the radar
		if (p1 == s1.length() && p2 == s2.length() && p1+p2 == s3.length()) {
			return true;
		}
		else if (p1 == s1.length() && p2 == s2.length() && p1+p2 < s3.length()) {
			// We have reached the end of s1 and s2 but there is still some left in s3 
			return false;
		}
		else if (p1+p2 == s3.length() && (p1<s1.length() || p2<s2.length())) {
			// We have reached the end of s3, but we still have some characters left over in s1 or s2
			return false;
		}

		if (visited[p1][p2]) {
			return dp[p1][p2];
		}

		bool isPossible = false;

		if (p1<s1.length() && p2<s2.length() && s3[p1+p2] == s1[p1] && s3[p1+p2] == s2[p2]) {
			// Character matches from both s1 and s2, so find choices 
			// Take it from s1
			isPossible = isPossible || checkInterleaving(p1+1, p2, s1, s2, s3);

			// Take it from s2
			isPossible = isPossible || checkInterleaving(p1, p2+1, s1, s2, s3);
		}
		else if (p1<s1.length() && s3[p1+p2] == s1[p1]) {
			isPossible = checkInterleaving(p1+1, p2, s1, s2, s3);
		}
		else if (p2<s2.length() && s3[p1+p2] == s2[p2]) {
			isPossible = checkInterleaving(p1, p2+1, s1, s2, s3);
		}

		dp[p1][p2] = isPossible;
        visited[p1][p2] = true;
		return isPossible;
	}
	
	bool isInterleave(string s1, string s2, string s3) {
		
		// Create a store for storing repeated computations
		dp.resize(s1.length()+1, vector<bool>(s2.length()+1));
		visited.resize(s1.length()+1, vector<bool>(s2.length()+1));

		return checkInterleaving(0, 0, s1, s2, s3);
	}
};
