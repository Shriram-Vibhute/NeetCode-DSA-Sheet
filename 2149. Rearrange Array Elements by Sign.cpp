class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int pivIndex = 0, nveIndex = 1;
        int n = nums.size();
        vector<int>newArr(n);

        for(int i = 0; i < n; i++) {
            if(nums[i] < 0) {
                newArr[nveIndex] = nums[i];
                nveIndex += 2;
            }
            else {
                newArr[pivIndex] = nums[i];
                pivIndex += 2;
            }
        }
        return newArr;
    }
};