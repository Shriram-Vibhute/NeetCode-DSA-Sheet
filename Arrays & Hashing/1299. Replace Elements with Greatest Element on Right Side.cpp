#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        int curr_max = arr[n - 1];

        for(int i = n - 2; i >= 0; i--){
            int curr_elem = arr[i];
            arr[i] = curr_max;
            curr_max = max(curr_elem, curr_max);
        }
        arr[n - 1] = -1;
        
        return arr;
    }
};