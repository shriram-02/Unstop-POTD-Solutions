
import java.io.*;
import java.util.*;

public class Main {

    static class FastScanner {
        private final InputStream in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;

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

        int nextInt() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= 32 && c != -1);

            int value = 0;
            while (c > 32 && c != -1) {
                value = value * 10 + c - '0';
                c = read();
            }
            return value;
        }
    }

    static class Fenwick {
        int n;
        long[] count;
        long[] sumP;
        long[] sumNext;
        long[] sumProduct;

        Fenwick(int n) {
            this.n = n;
            count = new long[n + 1];
            sumP = new long[n + 1];
            sumNext = new long[n + 1];
            sumProduct = new long[n + 1];
        }

        void add(int index, long p, long next) {
            long product = p * next;

            for (int i = index; i <= n; i += i & -i) {
                count[i]++;
                sumP[i] += p;
                sumNext[i] += next;
                sumProduct[i] += product;
            }
        }

        long[] query(int index) {
            long c = 0;
            long p = 0;
            long nx = 0;
            long product = 0;

            for (int i = index; i > 0; i -= i & -i) {
                c += count[i];
                p += sumP[i];
                nx += sumNext[i];
                product += sumProduct[i];
            }

            return new long[]{c, p, nx, product};
        }

        long[] rangeQuery(int left, int right) {
            long[] a = query(right);
            long[] b = query(left - 1);

            return new long[]{
                a[0] - b[0],
                a[1] - b[1],
                a[2] - b[2],
                a[3] - b[3]
            };
        }
    }

    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner(System.in);

        int m = fs.nextInt();
        int q = fs.nextInt();

        // Expand the run-length encoded sequence.
        int n = 0;
        int[] species = new int[200005];

        for (int i = 0; i < m; i++) {
            int code = fs.nextInt();
            int length = fs.nextInt();

            for (int j = 0; j < length; j++) {
                species[++n] = code;
            }
        }

        // Find the next occurrence of every position.
        int[] nextPos = new int[n + 1];

        HashMap<Integer, Integer> lastSeen = new HashMap<>();

        for (int i = n; i >= 1; i--) {
            int code = species[i];

            nextPos[i] = lastSeen.getOrDefault(code, n + 1);

            lastSeen.put(code, i);
        }

        // Bucket positions according to their next occurrence.
        int[] head = new int[n + 1];
        int[] link = new int[n + 1];

        Arrays.fill(head, -1);

        for (int p = 1; p <= n; p++) {
            int next = nextPos[p];

            if (next <= n) {
                link[p] = head[next];
                head[next] = p;
            }
        }

        // Store queries grouped by their right endpoint.
        int[] queryHead = new int[n + 1];
        int[] queryNext = new int[q];
        int[] queryLeft = new int[q];
        long[] answers = new long[q];

        Arrays.fill(queryHead, -1);

        for (int i = 0; i < q; i++) {
            int l = fs.nextInt();
            int r = fs.nextInt();

            queryLeft[i] = l;

            queryNext[i] = queryHead[r];
            queryHead[r] = i;
        }

        Fenwick bit = new Fenwick(n);

        StringBuilder out = new StringBuilder();

        // Sweep over right endpoints.
        for (int r = 1; r <= n; r++) {

            // Activate positions whose next occurrence is r.
            for (int p = head[r]; p != -1; p = link[p]) {
                bit.add(p, p, r);
            }

            // Answer all queries ending at r.
            for (int id = queryHead[r];
                 id != -1;
                 id = queryNext[id]) {

                int l = queryLeft[id];

                long length = r - l + 1L;

                // Base contribution.
                long base =
                    length * (length + 1) * (length + 2) / 6;

                // Query active positions in [l, r].
                long[] values = bit.rangeQuery(l, r);

                long count = values[0];
                long sumP = values[1];
                long sumNext = values[2];
                long sumProduct = values[3];

                // Calculate correction.
                long correction =
                    (long) (r + 1) *
                    (sumP - (long) (l - 1) * count)
                    -
                    (sumProduct - (long) (l - 1) * sumNext);

                answers[id] = base - correction;
            }
        }

        for (int i = 0; i < q; i++) {
            if (i > 0) out.append(' ');
            out.append(answers[i]);
        }

        out.append('\n');

        System.out.print(out);
    }
}