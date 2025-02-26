#include<queue>

class Solution {
public:
    void traverse(vector<vector<int>>& heightMap, vector<vector<int>>& waterToFill, int curMax, int i, int j,  int m, int n) {
            if (waterToFill[i][j] > curMax) {
                waterToFill[i][j] = curMax;
            }

            int curLevel = max(waterToFill[i][j], heightMap[i][j]);

            // Go Up
            if (i-1>0 && waterToFill[i-1][j]>curLevel) {
                traverse(heightMap, waterToFill, curLevel, i-1, j, m, n);
            }

            // Go Down
            if (i+1<m && waterToFill[i+1][j]>curLevel) {
                traverse(heightMap, waterToFill, curLevel, i+1, j, m, n);
            }

            // Go left
            if (j-1>0 && waterToFill[i][j-1]>curLevel) {
                traverse(heightMap, waterToFill, curLevel, i, j-1, m, n);
            }

            // Go right
            if (j+1<n && waterToFill[i][j+1]>curLevel) {
                traverse(heightMap, waterToFill, curLevel, i, j+1, m, n);
            }
    }

    int trapRainWater(vector<vector<int>>& heightMap) {
        int maxEle=0, i, j, m = heightMap.size(), n = heightMap[0].size();

        for (i=0;i<m;i++) {
            for (j=0;j<n;j++) {
                if (maxEle < heightMap[i][j]) {
                    maxEle = heightMap[i][j];
                }
            }
        }

        vector<vector<int>> waterToFill(m, vector<int>(n, maxEle));
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> queue;

        for (i=0;i<m;i++) {
            for(j=0;j<n;j++) {
                if (i>0 && i<m-1) {
                    if (j==0 || j==n-1) {
                        queue.push({heightMap[i][j], i, j});
                    }
                }
                else {
                    queue.push({heightMap[i][j], i, j});
                }
            }
        }

        while (!queue.empty()) {
            i = queue.top()[1];
            j = queue.top()[2];
            traverse(heightMap, waterToFill, heightMap[i][j], i, j, m, n);
            queue.pop();
        }

        int ans=0;
        for (i=1;i<m-1;i++) {
            for(j=1;j<n-1;j++) {
                ans += max(0, (waterToFill[i][j] - heightMap[i][j]));
            }
        }

        return ans;
    }
};
