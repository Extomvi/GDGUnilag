/*Palindrome Number */
/*Returns the value if the number given, N is a palindrome*/
class Solution {
    public boolean Palindrome (int n) {
        if(n < 0 || (n % 10 == 0 && n != 0)){
            return false;
        };
        int revertedNum = 0;
        while(n > revertedNum){
            int pop = n%10;
            revertedNum = revertedNum*10 + pop;
            n = n/10;
        }
    return n == revertedNum || n == revertedNum/10;
    }
    
};
