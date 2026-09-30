import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer firstLine = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(firstLine.nextToken());
        int m = Integer.parseInt(firstLine.nextToken());

        String belt = br.readLine().trim();

        int[] required = new int[26];
        StreamTokenizer tok = new StreamTokenizer(br);
        tok.wordChars('A', 'Z');
        for (int i = 0; i < m; i++) {
            tok.nextToken();
            char c = tok.sval.charAt(0);
            tok.nextToken();
            int count = (int) tok.nval;
            required[c - 'A'] += count; 
        }

        int typesNeeded = 0;
        for (int i = 0; i < 26; i++) {
            if (required[i] > 0) typesNeeded++;
        }

        int[] window = new int[26];
        int satisfied = 0;
        int left = 0;
        int minLen = Integer.MAX_VALUE;

        for (int right = 0; right < n; right++) {
            char c = belt.charAt(right);
            int idx = c - 'A';

            if (required[idx] > 0) {
                window[idx]++;
                if (window[idx] == required[idx]) {
                    satisfied++;
                }
            }

            while (satisfied == typesNeeded) {
                minLen = Math.min(minLen, right - left + 1);

                char lc = belt.charAt(left);
                int lidx = lc - 'A';
                if (required[lidx] > 0) {
                    if (window[lidx] == required[lidx]) {
                        satisfied--;
                    }
                    window[lidx]--;
                }
                left++;
            }
        }

        System.out.println(minLen == Integer.MAX_VALUE ? -1 : minLen);
    }
}