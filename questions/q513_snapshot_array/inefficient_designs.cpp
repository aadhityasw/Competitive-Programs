// Using 3D vector + pair
//TLE error

class SnapshotArray1 {
public:
    vector<int> arr;
    vector<vector<pair<int, int>>> store;

    SnapshotArray(int length) {
        arr.resize(length, 0);
    }
    
    void set(int index, int val) {
        arr[index] = val;
    }
    
    int snap() {
        vector<pair<int, int>> arrCopy;
        for (int i=0; i<arr.size(); i++) {
            if (arr[i] != 0) {
                arrCopy.push_back({i, arr[i]});
            }
        }
        store.push_back(arrCopy);
        return store.size()-1;
    }
    
    int get(int index, int snap_id) {
        int s=0, e=store[snap_id].size()-1;
        while (s <= e) {
            int m = s + (e-s)/2;
            if (store[snap_id][m].first < index) {
                s = m + 1;
            }
            else if (store[snap_id][m].first > index) {
                e = m - 1;
            }
            else {
                return store[snap_id][m].second;
            }
        }

        return 0;
    }
};





// 2D Vector and map implementation
// TLE


class SnapshotArray2 {
public:
    vector<int> arr;
    vector<map<int, int>> store;

    SnapshotArray(int length) {
        arr.resize(length, 0);
    }
    
    void set(int index, int val) {
        arr[index] = val;
    }
    
    int snap() {
        map<int, int> arrCopy;
        for (int i=0; i<arr.size(); i++) {
            if (arr[i] != 0) {
                arrCopy[i] = arr[i];
            }
        }
        store.push_back(arrCopy);
        return store.size()-1;
    }
    
    int get(int index, int snap_id) {
        auto ele = store[snap_id].find(index);
        if (ele != store[snap_id].end()) {
            return ele->second;
        }
        else {
            return 0;
        }
    }
};





// 2D Vector
//  Memory Limit Exceeded


class SnapshotArray {
public:
    vector<int> arr;
    vector<vector<int>> store;

    SnapshotArray(int length) {
        arr.resize(length, 0);
    }
    
    void set(int index, int val) {
        arr[index] = val;
    }
    
    int snap() {
        vector<int> arr2(arr.size());
        std::copy(arr.begin(), arr.end(), arr2.begin());
        store.push_back(arr2);
        return store.size()-1;
    }
    
    int get(int index, int snap_id) {
        return store[snap_id][index];
    }
};

