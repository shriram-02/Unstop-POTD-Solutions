import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }
        int s = 0;
        for(int i=1; i<n-1; i++) {
            if(arr[i] >= arr[i-1] && arr[i] >= arr[i+1]) {
               s = i;  
            }
        }
        if(s == 0) {
            System.out.println(n-1);
        } else {
            System.out.println(s);
        }
    }
}