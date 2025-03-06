class ProductOfNumbers {
    public:
        long distToZero;
        vector<double> store;
        double curProd;
        ProductOfNumbers() {
            curProd = 1;
            distToZero = -1;
        }
        
        void add(int num) {
            if (num != 0) {
                curProd = (double)(curProd * num);
                if (distToZero >= 0) {
                    distToZero ++;
                }
            }
            else {
                distToZero = 0;
                curProd = 1;
            }
            store.push_back(curProd);
        }
        
        int getProduct(int k) {
            double ans = 0;
            if (distToZero == -1 || distToZero >= k) {
                if (k >= store.size()) {
                    ans = curProd;
                }
                else {
                    ans = (store[store.size()-1] / store[store.size()-k-1]);
                }
            }
            return (int)ans;
        }
    };
    
    /**
     * Your ProductOfNumbers object will be instantiated and called as such:
     * ProductOfNumbers* obj = new ProductOfNumbers();
     * obj->add(num);
     * int param_2 = obj->getProduct(k);
     */
