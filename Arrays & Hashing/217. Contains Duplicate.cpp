#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*
    Three Approaches
    1. Hashing:
        Count the frequency of each character in both strings and compare the counts.
    2. Sorting:
        Sort both strings and check if they are identical.
    3. Length Comparison - Optimized:
        First check if lengths are equal length(set(array)) == length(array); if not, they can't be anagrams.
*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int>mpp;
        for(int i = 0; i < nums.size(); i++) {
            if(mpp.find(nums[i]) != mpp.end()) {
                return true;
            }
            mpp[nums[i]] = i;
        }
        return false;

        // You can simply compare the length of set and our array
        unordered_set<int> numSet(nums.begin(), nums.end());
        return numSet.size() < nums.size();
    }
};