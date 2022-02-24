/*Reverse string using two pointers */

class Solution {
    public void ReverseString(char[] str){
        int len = str.length;
        int left = 0;
        int right  = len - 1;
        while (left < right){
            char tmp = str[left];
            str[left] = str[right];
            str[right] = tmp;
            left++;
            right--;
        }
    }
    
}
