
import java.io.*;
import java.util.*;

public class Main {

    static final long INF = Long.MAX_VALUE / 4;
    static final int INF_COUNT = Integer.MAX_VALUE / 4;

    static class SegmentTree {
        int n;
        long[] tree;
        long[] lazy;
        int[] loads;

        SegmentTree(int n) {
            this.n = n;
            tree = new long[4 * n + 5];
            lazy = new long[4 * n + 5];
            loads = new int[4 * n + 5];

            Arrays.fill(tree, INF);
            Arrays.fill(loads, INF_COUNT);
        }

        void apply(int node, long value) {
            tree[node] += value;
            lazy[node] += value;
        }

        void push(int node) {
            if (lazy[node] != 0) {
                apply(node * 2, lazy[node]);
                apply(node * 2 + 1, lazy[node]);
                lazy[node] = 0;
            }
        }

        void pull(int node) {
            int left = node * 2;
            int right = left + 1;

            if (tree[left] < tree[right] ||
                (tree[left] == tree[right] &&
                 loads[left] < loads[right])) {

                tree[node] = tree[left];
                loads[node] = loads[left];

            } else {
                tree[node] = tree[right];
                loads[node] = loads[right];
            }
        }

        void update(int ql, int qr, long value) {
            if (ql > qr) return;
            update(1, 0, n - 1, ql, qr, value);
        }

        void update(int node, int left, int right,
                    int ql, int qr, long value) {

            if (ql > right || qr < left) return;

            if (ql <= left && right <= qr) {
                apply(node, value);
                return;
            }

            push(node);

            int mid = (left + right) / 2;

            update(node * 2, left, mid, ql, qr, value);
            update(node * 2 + 1, mid + 1, right,
                   ql, qr, value);

            pull(node);
        }

        void set(int index, long value, int count) {
            set(1, 0, n - 1, index, value, count);
        }

        void set(int node, int left, int right,
                 int index, long value, int count) {

            if (left == right) {
                tree[node] = value;
                loads[node] = count;
                lazy[node] = 0;
                return;
            }

            push(node);

            int mid = (left + right) / 2;

            if (index <= mid) {
                set(node * 2, left, mid,
                    index, value, count);
            } else {
                set(node * 2 + 1, mid + 1, right,
                    index, value, count);
            }

            pull(node);
        }

        Result query(int ql, int qr) {
            if (ql > qr) {
                return new Result(INF, INF_COUNT);
            }

            return query(1, 0, n - 1, ql, qr);
        }

        Result query(int node, int left, int right,
                     int ql, int qr) {

            if (ql <= left && right <= qr) {
                return new Result(tree[node], loads[node]);
            }

            push(node);

            int mid = (left + right) / 2;

            Result a = new Result(INF, INF_COUNT);
            Result b = new Result(INF, INF_COUNT);

            if (ql <= mid) {
                a = query(node * 2, left, mid, ql, qr);
            }

            if (qr > mid) {
                b = query(node * 2 + 1, mid + 1,
                          right, ql, qr);
            }

            if (a.waste < b.waste ||
                (a.waste == b.waste &&
                 a.loads < b.loads)) {
                return a;
            }

            return b;
        }
    }

    static class Result {
        long waste;
        int loads;

        Result(long waste, int loads) {
            this.waste = waste;
            this.loads = loads;
        }
    }

    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner(System.in);

        int n = fs.nextInt();
        int A = fs.nextInt();
        int B = fs.nextInt();

        long[] arr = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = fs.nextLong();
        }

        // Impossible if no valid partition can be formed.
        if (A <= 0 || B < A || n < A ||
            n > (long) n / A * B) {
            // The last condition is harmless; DP
            // below determines actual feasibility.
        }

        long[] dp = new long[n + 1];
        int[] count = new int[n + 1];

        Arrays.fill(dp, INF);
        Arrays.fill(count, INF_COUNT);

        dp[0] = 0;
        count[0] = 0;

        SegmentTree seg = new SegmentTree(n);

        int[] maxStack = new int[n];
        int[] minStack = new int[n];

        int maxTop = -1;
        int minTop = -1;

        for (int i = 0; i < n; i++) {

            // Insert the new possible starting position.
            seg.set(i, dp[i], count[i]);

            // Update maximum values of previous ranges.
            while (maxTop >= 0 &&
                   arr[maxStack[maxTop]] < arr[i]) {

                int p = maxStack[maxTop--];

                int left = (maxTop >= 0)
                        ? maxStack[maxTop] : -1;

                seg.update(left + 1, p,
                           arr[i] - arr[p]);
            }

            maxStack[++maxTop] = i;

            // Update minimum values of previous ranges.
            while (minTop >= 0 &&
                   arr[minStack[minTop]] > arr[i]) {

                int p = minStack[minTop--];

                int left = (minTop >= 0)
                        ? minStack[minTop] : -1;

                seg.update(left + 1, p,
                           arr[p] - arr[i]);
            }

            minStack[++minTop] = i;

            // Previous partition must have length [A, B].
            int L = Math.max(0, i + 1 - B);
            int R = i + 1 - A;

            if (L <= R) {

                Result best = seg.query(L, R);

                // Ignore unreachable DP states.
                if (best.waste < INF / 2) {
                    dp[i + 1] = best.waste;
                    count[i + 1] = best.loads + 1;
                }
            }
        }

        if (dp[n] >= INF / 2) {
            System.out.println("Cobalt plan: impossible");
        } else {
            System.out.println(
                "Cobalt plan: waste " + dp[n] +
                " with " + count[n] + " loads"
            );
        }
    }

    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];

        private int ptr = 0;
        private int len = 0;

        FastScanner(InputStream in) {
            this.in = in;
        }

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;

                if (len <= 0) return -1;
            }

            return buffer[ptr++];
        }

        long nextLong() throws IOException {
            int c;

            do {
                c = read();
            } while (c <= ' ' && c != -1);

            boolean negative = false;

            if (c == '-') {
                negative = true;
                c = read();
            }

            long value = 0;

            while (c > ' ') {
                value = value * 10 + c - '0';
                c = read();
            }

            return negative ? -value : value;
        }

        int nextInt() throws IOException {
            return (int) nextLong();
        }
    }
}