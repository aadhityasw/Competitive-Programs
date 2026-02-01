class Solution {
public:
    string minWindow(string s, string t) {
        int numSuccess = 0, numRequired=0;
        int front=0, rear=0;
        int ansSize = INT_MAX;
        string ans;

        vector<int> keyStore(128, 0);
        vector<int> store(128, 0);

        for (char ch : t) {
            keyStore[(int)ch] ++;
            if (keyStore[(int)ch] == 1) {
                numRequired ++;
            }
        }

        while (rear < s.length()) {
            store[(int)s[rear]] ++;
            if (store[(int)s[rear]] == keyStore[(int)s[rear]]) {
                numSuccess ++;
            }

            // If we have more than required characters in the window, then trim it
            while ((store[(int)s[front]] > keyStore[(int)s[front]]) && (front < rear)) {
                if (store[(int)s[front]] <= keyStore[(int)s[front]]) {
                    break;
                }
                store[(int)s[front]] --;
                front ++;
            }

            if (numSuccess == numRequired) {
                if (rear - front + 1 < ansSize) {
                    ans = "";
                    for (int i=front; i<=rear; i++) {
                        ans += s[i];
                    }
                    ansSize = ans.length();
                }

                while (numSuccess == numRequired) {
                    if (store[(int)s[front]] == keyStore[(int)s[front]]) {
                        numSuccess --;
                    }
                    store[(int)s[front]] --;
                    front ++;
                }
            }

            rear ++;
        }

        return ans;
    }
};
