class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        // Calculating total sum
        int total_sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            total_sum += nums[i];
        }

        int left_sum = 0;
        for(int i = 0; i < nums.size(); i++) {
            int right_sum = total_sum - nums[i] - left_sum;
            if(left_sum == right_sum) {
                return i;
            }
            left_sum += nums[i];
        }
        return -1;
    }
};