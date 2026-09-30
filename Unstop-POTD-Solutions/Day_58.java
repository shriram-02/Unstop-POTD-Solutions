import java.util.*;

public class Main {
    public static int findLuckyStonePairs(int p, int n, int m, int[] stones) {
        int validStones = 0;

        // Count how many stones match the divisibility rule
        for (int i = 0; i < p; i++) {
            if (stones[i] % n == 0 || stones[i] % m == 0) {
                validStones++;
            }
        }

        // If we don't have at least 2 valid stones, we can't form any pairs
        if (validStones < 2) {
            return 0;
        }

        // Calculate total unique pairs using n * (n - 1) / 2
        return (validStones * (validStones - 1)) / 2;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt();
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[] stones = new int[p];
        for (int i = 0; i < p; i++) {
            stones[i] = sc.nextInt();
        }
        
        int result = findLuckyStonePairs(p, n, m, stones);
        System.out.println(result);
    }
}