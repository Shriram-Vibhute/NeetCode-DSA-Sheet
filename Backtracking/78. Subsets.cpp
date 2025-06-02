# include <bits/stdc++.h>
using namespace std;

void generate_subsets(vector<int>& nums, vector<int>& arr, vector<vector<int>>& store, int i) {
    if (i == nums.size()) {
        store.push_back(arr);
        return ;
    }

    // Take
    arr.push_back(nums[i]);
    generate_subsets(nums, arr, store, i + 1);
    // Non Take
    arr.pop_back();
    generate_subsets(nums, arr, store, i + 1);

    return ;
}
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> store;
        vector<int> arr;
        generate_subsets(nums, arr, store, 0);
        return store;
    }
};