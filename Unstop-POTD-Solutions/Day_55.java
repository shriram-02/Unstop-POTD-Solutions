import java.util.*;

public class Main {
    public static int min_delivery_energy(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        if (grid[0][0] == -1 || grid[n - 1][m - 1] == -1) return -1;

        long[][] dist = new long[n][m];
        for (long[] row : dist) Arrays.fill(row, Long.MAX_VALUE);

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[2]));

        dist[0][0] = grid[0][0];
        pq.offer(new long[]{0, 0, grid[0][0]});

        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};

        while (!pq.isEmpty()) {
            long[] cur = pq.poll();
            int r = (int) cur[0];
            int c = (int) cur[1];
            long cost = cur[2];

            if (cost != dist[r][c]) continue;

            if (r == n - 1 && c == m - 1) return (int) cost;

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
                if (grid[nr][nc] == -1) continue;

                long newCost = cost + grid[nr][nc];

                if (newCost < dist[nr][nc]) {
                    dist[nr][nc] = newCost;
                    pq.offer(new long[]{nr, nc, newCost});
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        int[][] grid = new int[N][M];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                grid[i][j] = scanner.nextInt();
            }
        }

        int result = min_delivery_energy(grid);
        System.out.println(result);
    }
}