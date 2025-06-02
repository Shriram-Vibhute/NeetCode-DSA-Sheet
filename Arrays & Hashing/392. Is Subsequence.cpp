#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int m = s.length();
        int n = t.length();
        if (m > n) return false;

        int i = 0; 
        int j = 0;
        while(i < m && j < n) {
            if(s[i] == t[j]) {
                i += 1;
                j += 1;
            }
            else {
                j += 1;
            }
        }
        if(i >= m) {
            return true;
        }
        return false;
    }
};