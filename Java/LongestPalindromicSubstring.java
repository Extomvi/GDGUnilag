class Solution{
    public String LongestPalindromicSubstring(String str) {
        public String LongestPalindromicSubstring(String str) {
            if(str == null || str.length() < 1){
                return "";
            }
            int start = 0;
            int end = 0;
            for(int i = 0; i < str.length(); i++){
                int len1 = expandAroundCenter(str,i,i);
                int len2 = expandAroundCenter(str,i,i+1);
                int len = max(len1, len2);

                if(len > end - start){
                    start = i - (len -1)/2;
                    end = i + len/2;
                }

            }
            return str.substring(start, end+1);
        }        

        private int expandAroundCenter(String str, int left, int right){
            int L = left;
            int R = right;
            while(L>=0 && R<str.length() && str.charAt(L) == str.charAt(R)){
                L--;
                R++;
            }
            return R - L - 1;
        }
            
    }

}

