#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.length();
        int counter_space = 0, i = n - 1;
        bool check = false;

        while(i >= 0){
            if(check && s[i] == ' ') break;
            if(s[i] == ' ') counter_space++;
            else check = true;
            i -= 1;
        }

        if(counter_space == n) return 0;
        return n - counter_space - i - 1;
    }
};