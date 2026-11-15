import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class Main {

    static final int ROOT = 1;
    static final int FIRST = 0;
    static final int MAX_DIGITS = 24;

    static class MaxHeap {
        final long[] data;
        int size = 0;

        MaxHeap(int cap) {
            data = new long[cap + 2];
        }

        long peek() {
            return data[ROOT];
        }

        void push(long val) {
            int i = ++size;
            while (i > 1) {
                int p = i >> 1;
                if (data[p] < val) {
                    data[i] = data[p];
                    i = p;
                } else {
                    break;
                }
            }
            data[i] = val;
        }

        long pop() {
            long top = data[ROOT];
            long last = data[size--];
            int i = ROOT;
            while ((i << 1) <= size) {
                int c = i << 1;
                if (c + 1 <= size && data[c + 1] > data[c]) {
                    c++;
                }
                if (data[c] > last) {
                    data[i] = data[c];
                    i = c;
                } else {
                    break;
                }
            }
            if (size > 0) {
                data[i] = last;
            }
            return top;
        }
    }

    static class MinHeap {
        final long[] data;
        int size = 0;

        MinHeap(int cap) {
            data = new long[cap + 2];
        }

        long peek() {
            return data[ROOT];
        }

        void push(long val) {
            int i = ++size;
            while (i > 1) {
                int p = i >> 1;
                if (data[p] > val) {
                    data[i] = data[p];
                    i = p;
                } else {
                    break;
                }
            }
            data[i] = val;
        }

        long pop() {
            long top = data[ROOT];
            long last = data[size--];
            int i = ROOT;
            while ((i << 1) <= size) {
                int c = i << 1;
                if (c + 1 <= size && data[c + 1] < data[c]) {
                    c++;
                }
                if (data[c] < last) {
                    data[i] = data[c];
                    i = c;
                } else {
                    break;
                }
            }
            if (size > 0) {
                data[i] = last;
            }
            return top;
        }
    }

    public static void main(String[] args) throws IOException {
        FastScanner sc = new FastScanner(System.in);
        FastWriter out = new FastWriter(System.out);

        int n = sc.nextInt();
        int q = sc.nextInt();

        MaxHeap L = new MaxHeap(n + 2);
        MinHeap R = new MinHeap(n + 2);

        long addL = 0;
        long addR = 0;
        long minVal = 0;

        // Round 1
        long lo1 = sc.nextLong();
        long hi1 = sc.nextLong();
        L.push(lo1);
        R.push(hi1);

        // Rounds 2 to n
        for (int i = 2; i <= n; i++) {
            long lo = sc.nextLong();
            long hi = sc.nextLong();
            long up = sc.nextLong();
            long down = sc.nextLong();

            addL -= down;
            addR += up;

            // Add max(0, lo - x)
            long minR = R.peek() + addR;
            if (lo <= minR) {
                L.push(lo - addL);
            } else {
                minVal += lo - minR;
                R.pop();
                R.push(lo - addR);
                L.push(minR - addL);
            }

            // Add max(0, x - hi)
            long maxL = L.peek() + addL;
            if (hi >= maxL) {
                R.push(hi - addR);
            } else {
                minVal += maxL - hi;
                L.pop();
                L.push(hi - addL);
                R.push(maxL - addR);
            }
        }

        long bestCoord = L.peek() + addL;
        out.printLong(minVal);
        out.printSpace();
        out.printLong(bestCoord);
        out.println();

        // Extract sorted breakpoints directly from heaps in O(n log n)
        long[] leftPts = new long[n];
        long[] rightPts = new long[n];
        for (int i = 0; i < n; i++) {
            leftPts[n - 1 - i] = L.pop() + addL;
            rightPts[i] = R.pop() + addR;
        }

        long[] prefL = new long[n + 1];
        long[] prefR = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefL[i + 1] = prefL[i] + leftPts[i];
            prefR[i + 1] = prefR[i] + rightPts[i];
        }

        long maxLeftPt = leftPts[n - 1];
        long minRightPt = rightPts[FIRST];

        for (int i = 0; i < q; i++) {
            long z = sc.nextLong();
            long ans = minVal;

            if (z < maxLeftPt) {
                int idx = upperBound(leftPts, z);
                long count = n - idx;
                ans += (prefL[n] - prefL[idx]) - count * z;
            } else if (z > minRightPt) {
                int idx = lowerBound(rightPts, z);
                long count = idx;
                ans += count * z - prefR[idx];
            }

            out.printLong(ans);
            out.println();
        }

        out.flush();
    }

    static int upperBound(long[] arr, long target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    static int lowerBound(long[] arr, long target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    static final class FastScanner {
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

        int nextInt() throws IOException {
            return (int) nextLong();
        }

        long nextLong() throws IOException {
            int c = read();
            while (c <= 32) {
                if (c == -1) return 0;
                c = read();
            }
            long sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            long res = 0;
            while (c > 32) {
                res = res * 10 + (c - '0');
                c = read();
            }
            return res * sign;
        }
    }

    static final class FastWriter {
        private final OutputStream out;
        private final byte[] buffer = new byte[1 << 16];
        private final byte[] numBuf = new byte[MAX_DIGITS];
        private int ptr = 0;

        FastWriter(OutputStream out) {
            this.out = out;
        }

        void printSpace() throws IOException {
            if (ptr == buffer.length) flushBuffer();
            buffer[ptr++] = ' ';
        }

        void println() throws IOException {
            if (ptr == buffer.length) flushBuffer();
            buffer[ptr++] = '\n';
        }

        void printLong(long x) throws IOException {
            if (x == 0) {
                if (ptr == buffer.length) flushBuffer();
                buffer[ptr++] = '0';
                return;
            }
            if (x < 0) {
                if (ptr == buffer.length) flushBuffer();
                buffer[ptr++] = '-';
                x = -x;
            }
            int len = 0;
            while (x > 0) {
                numBuf[len++] = (byte) ('0' + (x % 10));
                x /= 10;
            }
            while (len > 0) {
                if (ptr == buffer.length) flushBuffer();
                buffer[ptr++] = numBuf[--len];
            }
        }

        private void flushBuffer() throws IOException {
            out.write(buffer, 0, ptr);
            ptr = 0;
        }

        void flush() throws IOException {
            flushBuffer();
            out.flush();
        }
    }
}