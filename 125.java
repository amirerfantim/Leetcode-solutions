class Soultion125 {
    public static boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z]", "").toLowerCase();
        int start = 0;
        int end = s.length()-1;
        while (start < end){
            if (s.charAt(start) != s.charAt(end)){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

}