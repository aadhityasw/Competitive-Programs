class Solution {
public:
    int getModified(int num) {
        int sign = (num >= 0)? 1 : -1;
        num*= sign;

        if (int(num%10000) >= 9000 && int(num%10000) < 10000) {
            num += 10000;
        }
        
        int ans = sign * int(num/10000);
        return ans;
    }

    int getOriginal(int num) {
        if (num >= -1000 && num <= 1000) {
            return num;
        }

        int sign = (num >= 0)? 1 : -1;
        num*= sign;

        num = num % 10000;
        if (num >= 9000) {
            num -= 10000;
        }

        return num;
    }

    int encode(int src, int dest) {
        int s = 1;
        if (src < 0) {
            s = -1;
        }

        int ans = s * ((s*src)*10000 + dest);
        return ans;
    }

    void rotate(vector<vector<int>>& matrix) {
        int n=matrix.size()-1, src, dest;
        bool isPos=true;
        for(int i=0; i<=n; i++) {
            for(int j=0; j<=n; j++) {
                src = getOriginal(matrix[n-j][i]);
                dest = getOriginal(matrix[i][j]);

                matrix[i][j] = encode(src, dest);
            }
        }

        for (int i=0; i<=n; i++) {
            for(int j=0; j<=n; j++) {
                matrix[i][j] = getModified(matrix[i][j]);
            }
        }
    }
};
