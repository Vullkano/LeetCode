class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }

        int reversed = 0;
        int original = x;

        while (x != 0) {
            int digit = x % 10; // Obtém o último dígito de x
            System.out.println("Dígito: " + digit);
            reversed = reversed * 10 + digit; // Constrói o número invertido
            System.out.println("Reversed: " + reversed);
            x /= 10; // Remove o último dígito de x (por x ser int)
            System.out.println("x: " + x);
        }

        return original == reversed; // Compara o número original com o invertido
    }
}