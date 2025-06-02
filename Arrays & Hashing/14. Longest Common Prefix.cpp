# include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int str_len = strs[0].length();
        string longest_prefix = "";

        for(int i = 0; i < str_len; i++) {
            char curr_char = strs[0][i];
            int j = 1;
            for (j = 1; j < strs.size(); j++) {
                if (i >= strs[j].length() || curr_char != strs[j][i]) {
                    return longest_prefix;
                }
            }
            longest_prefix += curr_char;
        }

        return longest_prefix;
    }
};