class Solution {
    public:
    
        static bool compareEntries(vector<int>& a, vector<int>& b) {
            if (a[0] == b[0]) {
                return a[1] < b[1];
            }
            return a[0] > b[0];
        }
    
        vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
            
            // Sort in descending order of heights
            sort(people.begin(), people.end(), compareEntries);
    
            // Create a result array
            vector<vector<int>> result;
    
            // Get the number of people
            int numPeople = people.size();
    
            // Insert the elements in the right position in the array
            for (int i=0; i<numPeople; i++) {
                result.insert(result.begin()+people[i][1], people[i]);
            }
    
            return result;
        }
    };
