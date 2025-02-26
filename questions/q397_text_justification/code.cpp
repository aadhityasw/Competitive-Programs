#include <cmath>

class Solution {
public:
    string leftJustify(vector<string>&words, int start, int end, int maxWidth) {
        int words_len = 0;
        string ans="";
        for (int i=start;i<end;i++) {
            words_len += words[i].length();
            ans += words[i];
            if (i < end-1) {
                ans += " ";
                words_len += 1;
            }
        }
        for (int i=words_len;i<maxWidth;i++) {
            ans += " ";
        }
        return ans;
    }

    string centerJustify(vector<string>&words, int start, int end, int maxWidth) {
        if (end-start == 1) {
            return leftJustify(words, start, end, maxWidth);
        }

        int i, words_len=0;
        for(i=start;i<end;i++) {
            words_len += words[i].length();
        }

        int spaces_bet = int(floor((maxWidth-words_len) / (end-start-1)));
        int remaining_spaces = (maxWidth-words_len) % (end-start-1);
        string ans = "";

        for (i=start;i<end;i++) {
            ans += words[i];
            if (i < end-1) {
                for (int j=0;j<spaces_bet;j++) {
                    ans += " ";
                }
                if (remaining_spaces > 0) {
                    ans += " ";
                    remaining_spaces--;
                }
            }
            
        }
        return ans;
    }

    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        int i=0, start=0, cur_sum=0;

        while (i <= words.size()) {
            if (i == words.size() && i!= start) {
                ans.push_back(leftJustify(words, start, i, maxWidth));
                break;
            }
            else if (i == words.size()) {
                break;
            }

            cur_sum += words[i].length();
            if (cur_sum == maxWidth) {
                ans.push_back(centerJustify(words, start, i+1, maxWidth));
                start = i+1;
                i+=1;
                cur_sum = 0;
            }
            else if (cur_sum > maxWidth) {
                ans.push_back(centerJustify(words, start, i, maxWidth));
                start = i;
                cur_sum = 0;
            }
            else {
                cur_sum += 1; // for space between words
                i++;
            }
        }

        return ans;
    }
};
