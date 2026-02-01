class Solution {
public:
    int nextGreaterElement(int n) {
        long num = n;
        stack<int> s1;

        int dig = -1;
        while (num > 0 && (num%10) >= dig) {
            dig = num %10;
            s1.push(dig);
            num = num / 10;
        }

        if (num == 0) {
            return -1;
        }
        dig = num % 10;
        num = num / 10;

        stack<int> s2;
        while (!s1.empty() && s1.top() > dig) {
            s2.push(s1.top());
            s1.pop();
        }
        s1.push(dig);

        num = (num * 10) + s2.top();
        s2.pop();

        while (!s1.empty()) {
            s2.push(s1.top());
            s1.pop();
        }

        while (!s2.empty()) {
            num = (num * 10) + s2.top();
            s2.pop();
        }

        if (num > INT_MAX) {
            return -1;
        }
        return (int)num;
    }
};
