class SnapshotArray {
public:
    vector<vector<pair<int, int>>> arr;
    int curSnapId;

    SnapshotArray(int length) {
        arr.resize(length);
        curSnapId = 0;
    }
    
    void set(int index, int val) {
        if (arr[index].size() == 0 || arr[index][arr[index].size()-1].first < curSnapId) {
            arr[index].push_back({curSnapId, val});
        }
        else {
            arr[index][arr[index].size()-1].second = val;
        }
    }
    
    int snap() {
        return curSnapId++;
        
    }
    
    int get(int index, int snap_id) {
        int s=0, e=arr[index].size()-1;
        while (s <= e) {
            int m = s + (e-s)/2;
            if (arr[index][m].first < snap_id) {
                s = m + 1;
            }
            else if (arr[index][m].first > snap_id) {
                e = m - 1;
            }
            else {
                return arr[index][m].second;
            }
        }

        if (e >= 0) {
            return arr[index][e].second;
        }
        return 0;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
