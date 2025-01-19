class Solution {
    public int lengthOfLastWord(String s) {
        String[] myArray = s.trim().split(" ");
        String last = myArray[myArray.length - 1];
        return last.length();
    }
}