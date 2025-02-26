class Solution {
    public:
        double calculateAreaDiff(double mid, vector<vector<int>>& squares) {
            double area = 0.0;
    
            for (int i=0; i<squares.size(); i++) {
                if (squares[i][1] < mid && (squares[i][1]+squares[i][2]) > mid) {
                    area += (2*squares[i][1] + squares[i][2] - 2*mid)*squares[i][2];
                }
                else if (squares[i][1] >= mid ) {
                    area += ((double)(squares[i][2]) * (double)(squares[i][2]));
                }
                else {
                    area -= ((double)(squares[i][2]) * (double)(squares[i][2]));
                }
            }
            return area;
        }
    
        double separateSquares(vector<vector<int>>& squares) {
            double top=-1, bottom=INT_MAX;
    
            for (int i=0; i< squares.size(); i++) {
                if (top < squares[i][1]+squares[i][2]) {
                    top = squares[i][1]+squares[i][2];
                }
                if (bottom > squares[i][1]) {
                    bottom = squares[i][1];
                }
            }
            double mid=0;
    
            while (top-bottom > 0.000001) {
                mid = (bottom+top)/2.0;
                double diffArea = calculateAreaDiff(mid, squares);
    
                if (diffArea > 0) {
                    bottom = mid;
                }
                else {
                    top = mid;
                }
            }
    
            return mid;
        }
};
