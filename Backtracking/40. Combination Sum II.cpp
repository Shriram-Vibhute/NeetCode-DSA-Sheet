# include <bits/stdc++.h>
using namespace std;

void find_unique_combinations(vector<int>& candidates, vector<int> &arr, vector<vector<int>> &store, int i, int curr_sum, int target) {
    // Base Case
    if (curr_sum == target) {
        store.push_back(arr);
        return ;
    }

    if (i >= candidates.size() || curr_sum > target) {
        return ;
    }

    // Recursion
    arr.push_back(candidates[i]);
    find_unique_combinations(candidates, arr, store, i + 1, curr_sum + candidates[i], target);
    arr.pop_back();
    while (i + 1 < candidates.size() && candidates[i] == candidates[i + 1]) {
        i++;
    }
    find_unique_combinations(candidates, arr, store, i + 1, curr_sum, target);
    
    return;
}
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> arr;
        vector<vector<int>> store;
        find_unique_combinations(candidates, arr, store, 0, 0, target);

        return store;
    }
};