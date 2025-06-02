# include <bits/stdc++.h>
using namespace std;

void dfs(vector<int>& candidates, vector<int>& arr, vector<vector<int>>& store, int i, int curr_sum, int target) {
    // Base Cases
    if(target == curr_sum) {
        store.push_back(arr);
        return;
    }
    if (target < curr_sum || i >= candidates.size()) return;

    arr.push_back(candidates[i]);
    dfs(candidates, arr, store, i, curr_sum + candidates[i], target);
    arr.pop_back();
    dfs(candidates, arr, store, i + 1, curr_sum, target);

    return;
}
class Solution { 
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int>arr;
        vector<vector<int>>store;
        dfs(candidates, arr, store, 0, 0, target);
        return store;
    }
};