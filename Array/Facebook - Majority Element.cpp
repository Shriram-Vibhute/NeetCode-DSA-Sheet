// Moore's Voting Algorithm
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int element = 0;
        int n = nums.size();

        for(int i = 0; i < n; i++) {
            if(count == 0) element = nums[i];

            // We cant write below two lines above
            if(nums[i] == element) count++;
            else count--;
        }
        int countRecheck = 0;
        for(int i = 0; i < n; i++) {
            if(nums[i] == element) countRecheck++;
        }
        return (countRecheck > n/2) ? element : -1;
    }
};