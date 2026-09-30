import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class Main {
    public static void user_logic(int t, List<int[]> test_cases) {
        for (int[] arr : test_cases) {
            StringBuilder sb = new StringBuilder();

            int idx = 0;
            while (idx < arr.length) {
                sb.append(arr[idx]).append(" ");
                idx = 2 * idx + 1; 
            }

            System.out.println(sb.toString().trim());
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        List<int[]> test_cases = new ArrayList<>();

        for (int i = 0; i < t; i++) {
            int N = sc.nextInt();
            int number_of_nodes = (1 << N) - 1;
            int[] arr = new int[number_of_nodes];
            for (int j = 0; j < number_of_nodes; j++) {
                arr[j] = sc.nextInt();
            }
            test_cases.add(arr);
        }
        user_logic(t, test_cases);
    }
}