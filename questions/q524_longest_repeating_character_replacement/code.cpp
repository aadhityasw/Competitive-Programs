class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> store(26, 0);
        int front = -1, rear = 0;
        int maxSize = 0;

        while (rear < s.length()) {
            store[(int)s[rear]-65] ++;
            int numChar = (rear - front);
            int maxFreq = 0;
            for (int f : store) {
                maxFreq = max(maxFreq, f);
            }
            int numToReplace = numChar - maxFreq;

            while (numToReplace > k && front <= rear) {
                front ++;
                store[(int)s[front]-65] --;
                numChar = (rear - front);
                maxFreq = 0;
                for (int f : store) {
                    maxFreq = max(maxFreq, f);
                }
                numToReplace = numChar - maxFreq;
            }

            maxSize = max(maxSize, (rear - front));
            rear ++;
        }

        return maxSize;
    }
};
