#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        // Optimization
        if (s.length() != t.length())
            return false;

        // For storing the counts of characters
        vector<int> counter(26, 0);

        // Solution
        for (int i = 0; i < s.size(); i++)
        {
            counter[s[i] - 'a'] += 1;
        }
        for (int i = 0; i < s.size(); i++)
        {
            if (counter[t[i] - 'a'] == 0)
                return false;
            else
            {
                counter[t[i] - 'a'] -= 1;
            }
        }
        return true;
    }
};