class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) return s.length();
        String verificar = "";
        int longest = 0;
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (!verificar.contains(String.valueOf(current))) {
                verificar += current;
                longest = Math.max(longest, verificar.length());
            } else {
                if (String.valueOf(current).equals(String.valueOf(verificar.charAt(verificar.length() - 1)))) {
                    verificar = String.valueOf(current);
                } else {
                    int index = verificar.indexOf(String.valueOf(current));
                    verificar = verificar.substring(index + 1) + current;
                }
            }
        }
        return longest;
    }
}