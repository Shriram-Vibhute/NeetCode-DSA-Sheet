#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int appendCharacters(string s, string t) {
        // s is superset and t is subset
        int m = s.length(), n = t.length();
        int i = 0, j = 0;

        while(i < m && j < n) {
            if(s[i] == t[j]) {
                i += 1;
                j += 1;
            }
            else {
                i += 1;
            }
        }

        return (j >= n) ? 0 : n - j;
    }
};