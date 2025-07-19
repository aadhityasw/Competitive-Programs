class Solution {
public:
    vector<int> parent;

    int findParent(int pos) {
        while (parent[pos] != pos) {
            pos = parent[pos];
        }
        return pos;
    }

    void updateParent(int pos, int p) {
        if (pos != p) {
            int ch = parent[pos];
            parent[pos] = p;
            updateParent(ch, p);
        }
    }

    string smallestEquivalentString(string s1, string s2, string baseStr) {
        parent.resize(26);
        for (int i=0; i<26; i++) {
            parent[i] = i;
        }

        for (int i=0; i<s1.length(); i++) {
            int p1 = findParent(int(s1[i])-97);
            int p2 = findParent(int(s2[i])-97);
            updateParent(int(s1[i])-97, min(p1, p2));
            updateParent(int(s2[i])-97, min(p1, p2));
        }

        for (int i=0; i<26; i++) {
            int p = findParent(i);
            updateParent(i, p);
        }

        string ans = "";
        for (char ch : baseStr) {
            ans += (char)(parent[int(ch)-97] + 97);
        }
        return ans;
    }
};
