import java.util.Scanner;

public class Main {
    static long user_logic(int n, long[] capacity, long[] load) {
        long totalCapacity = 0;
        long totalLoad = 0;

        for (int i = 0; i < n; i++) {
            totalCapacity += capacity[i];
            totalLoad += load[i];
        }

        if (totalLoad > totalCapacity) return -1;

        long overload = 0;

        for (int i = 0; i < n; i++) {
            if (load[i] > capacity[i]) {
                overload += (load[i] - capacity[i]);
            }
        }

        return overload;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        long[] capacity = new long[n];
        long[] load = new long[n];

        for (int i = 0; i < n; i++) {
            capacity[i] = scanner.nextLong();
        }

        for (int i = 0; i < n; i++) {
            load[i] = scanner.nextLong();
        }

        long result = user_logic(n, capacity, load);
        System.out.println(result);
    }
}