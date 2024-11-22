class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i = 0;
        if(flowerbed.size() == 1 && flowerbed[i] == 0) {
            flowerbed[i] = 1;
            n--;
            i++;
        }
        while(n > 0 && i < flowerbed.size()) {
            if(flowerbed[i] != 1) {
                if(i == 0) {
                    if(flowerbed[i + 1] != 1){
                        n--;
                        flowerbed[i] = 1;
                    } 
                }
                else if(i == flowerbed.size() - 1 ) {
                    if(flowerbed[i - 1] != 1) {
                        n--;
                        flowerbed[i] = 1;
                    }
                }
                else {
                    if(flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0) {
                        flowerbed[i] = 1;
                        n--;
                    }
                }
                i += 1;
            }
            else {
                i += 2;
            }
        }

        if(n <= 0) return true;
        return false;
    }
};