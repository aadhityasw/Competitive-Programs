class MovingAverage {
    public:
        queue<int> window;
        int winSize;
        int winSum, maxWinSize;
        MovingAverage(int size) {
            winSize=0;
            winSum=0;
            maxWinSize=size;
        }
        
        double next(int val) {
            if (winSize == maxWinSize) {
                winSum -= window.front();
                window.pop();
            }
            else {
                winSize++;
            }
            window.push(val);
            winSum += val;
            return ((double)winSum/winSize);
        }
    };
    
    /**
     * Your MovingAverage object will be instantiated and called as such:
     * MovingAverage* obj = new MovingAverage(size);
     * double param_1 = obj->next(val);
     */
