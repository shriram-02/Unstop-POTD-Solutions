import java.util.*;

public class Main {
    static boolean isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }

    public static long talentBurst(int[] arr) {
        int n = arr.length;
        int[] v = new int[n + 2];
        v[0] = 1;
        v[n + 1] = 1;
        for (int i = 0; i < n; i++) v[i + 1] = arr[i];

        long[][] dp = new long[n + 2][n + 2];

        for (int len = 2; len < n + 2; len++) {
            for (int l = 0; l + len < n + 2; l++) {
                int r = l + len;
                long best = 0;
                for (int i = l + 1; i < r; i++) {
                    long gain = (long) (v[l] + 2) * v[i] * (v[r] + 2);
                    if (isPrime(v[i])) gain += v[i];
                    best = Math.max(best, dp[l][i] + dp[i][r] + gain);
                }
                dp[l][r] = best;
            }
        }

        return dp[0][n + 1];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(talentBurst(arr));
    }
}