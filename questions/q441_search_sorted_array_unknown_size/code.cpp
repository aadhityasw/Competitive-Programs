/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     int get(int index);
 * };
 */

 class Solution {
    public:
        int search(const ArrayReader& reader, int target) {
            int low = 0, high=10000, mid;
            while (low < high) {
                mid = (low+high)/2;
                int indVal = reader.get(mid);
                if (indVal == INT_MAX) {
                    high = mid-1;
                }
                else if (indVal == target) {
                    return mid;
                }
                else if (indVal > target) {
                    high = mid-1;
                }
                else {
                    low = mid+1;
                }
            }
            
            return (reader.get(low)==target) ? low : -1;
        }
    };
