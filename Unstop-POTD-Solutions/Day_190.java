
import java.io.*;
import java.util.*;

public class Main {

    static class Fenwick {
        int n;
        long[] tree;

        Fenwick(int n) {
            this.n = n;
            tree = new long[n + 1];
        }

        void update(int index, long value) {
            while (index <= n) {
                tree[index] += value;
                index += index & -index;
            }
        }

        long query(int index) {
            long sum = 0;

            while (index > 0) {
                sum += tree[index];
                index -= index & -index;
            }

            return sum;
        }

        // Returns the smallest index whose prefix sum >= k
        int findKth(long k) {
            int index = 0;

            int bit = Integer.highestOneBit(n);

            for (; bit > 0; bit >>= 1) {
                int next = index + bit;

                if (next <= n && tree[next] < k) {
                    index = next;
                    k -= tree[next];
                }
            }

            return index + 1;
        }
    }

    static long sumSmallest(
            long k,
            Fenwick countTree,
            Fenwick sumTree,
            int[] values
    ) {
        if (k == 0) {
            return 0;
        }

        int index = countTree.findKth(k);

        long countBefore = countTree.query(index - 1);
        long sumBefore = sumTree.query(index - 1);

        long remainingCopies = k - countBefore;

        return sumBefore + remainingCopies * values[index - 1];
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in)
        );

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        long W = Long.parseLong(st.nextToken());

        long[] times = new long[n];
        int[] readings = new int[n];

        int[] sortedValues = new int[n];

        for (int i = 0; i < n; i++) {

            st = new StringTokenizer(br.readLine());

            times[i] = Long.parseLong(st.nextToken());
            readings[i] = Integer.parseInt(st.nextToken());

            sortedValues[i] = readings[i];
        }

        // Coordinate compression
        Arrays.sort(sortedValues);

        int m = 0;

        for (int i = 0; i < n; i++) {
            if (m == 0 || sortedValues[i] != sortedValues[m - 1]) {
                sortedValues[m++] = sortedValues[i];
            }
        }

        int[] values = Arrays.copyOf(sortedValues, m);

        // Two Fenwick Trees
        Fenwick countTree = new Fenwick(m);
        Fenwick sumTree = new Fenwick(m);

        long totalSum = 0;
        long activeCount = 0;

        int addPtr = 0;
        int removePtr = 0;

        StringBuilder output = new StringBuilder();

        for (int j = 0; j < q; j++) {

            st = new StringTokenizer(br.readLine());

            long t = Long.parseLong(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            // Add all readings available by time t
            while (addPtr < n && times[addPtr] <= t) {

                int value = readings[addPtr];

                int index = Arrays.binarySearch(values, value) + 1;

                countTree.update(index, 1);
                sumTree.update(index, value);

                totalSum += value;
                activeCount++;

                addPtr++;
            }

            // Remove expired readings
            while (removePtr < addPtr &&
                   times[removePtr] <= t - W) {

                int value = readings[removePtr];

                int index = Arrays.binarySearch(values, value) + 1;

                countTree.update(index, -1);
                sumTree.update(index, -value);

                totalSum -= value;
                activeCount--;

                removePtr++;
            }

            // No fresh readings
            if (activeCount == 0) {
                output.append("NO DATA\n");
                continue;
            }

            // Number of readings removed from each end
            long k = (activeCount * p) / 100;

            long remaining = activeCount - 2 * k;

            // Sum of smallest k readings
            long smallestSum = sumSmallest(
                    k, countTree, sumTree, values
            );

            // Sum of largest k readings
            long largestSum = sumSmallest(
                    k, countTree, sumTree, values
            );

            // Sum of all remaining readings
            // Largest k sum = totalSum - sum of smallest activeCount-k
            largestSum = totalSum -
                    sumSmallest(
                            activeCount - k,
                            countTree,
                            sumTree,
                            values
                    );

            long trimmedSum = totalSum - smallestSum - largestSum;

            // Smallest remaining reading: (k+1)th smallest
            int minIndex = countTree.findKth(k + 1);
            int minKept = values[minIndex - 1];

            // Largest remaining reading: (activeCount-k)th smallest
            int maxIndex = countTree.findKth(activeCount - k);
            int maxKept = values[maxIndex - 1];

            output.append(remaining).append(" ")
                  .append(trimmedSum).append(" ")
                  .append(minKept).append(" ")
                  .append(maxKept).append("\n");
        }

        System.out.print(output);
    }
}