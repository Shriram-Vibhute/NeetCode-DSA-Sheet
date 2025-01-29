class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // The task is to converget the two arrys into nums1
        // Merge algorithm
        vector<int>store;

        int i = 0, j = 0;
        while(i < m && j < n) {
            if(nums1[i] <= nums2[j]) {
                store.push_back(nums1[i]);
                i++;
            }
            else {
                store.push_back(nums2[j]);
                j++;
            }
        }

        while(i < m) {
            store.push_back(nums1[i]);
                i++;
        }
        while(j < n) {
            store.push_back(nums2[j]);
                j++;
        }

        for(int i = 0; i < store.size(); i++) {
            nums1[i] = store[i];
        }
    }
};