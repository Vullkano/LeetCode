class Solution {
    String longestCommonPrefix(String[] strs) {
        int lengthLista = strs.length;
        if (lengthLista == 0){
            return "";
        }
        int palavraMaisCurta = Collections.min(List.of(strs), Comparator.comparingInt(String::length)).length();
        String prefix = "";

        for (int j = 0; j < palavraMaisCurta; j++) {
            for (int i = 0; i < lengthLista; i++) {
                if (strs[0].charAt(j) != strs[i].charAt(j)) {
                    return prefix;
                }
            }
            prefix += strs[0].charAt(j);
        }
        return prefix;
    }
}