class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.size() != t.size()) return false;

        unordered_map<char, char>mpp; // For mapping the characters
        unordered_set<char>st; 
        // Test cases like -> s = badc | t = baba in which the characters of t are doubly linked with s characters
        
        for(int i = 0; i < s.size(); i++) {
            if(mpp.find(s[i]) != mpp.end()) {
                if(mpp[s[i]] != t[i]) {
                    return false;
                }
            }
            else if(st.find(t[i]) != st.end()) {
                return false;
            }
            else {
                mpp[s[i]] = t[i];
                st.insert(t[i]);
            }
        }
        return true;
    }
};