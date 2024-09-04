/*
Easy Subarray Sum
*/

import java.util.Scanner;

public class Codechef_EasySubarray {
    public static void main(String[] args) throws java.lang.Exception {
        // your code goes here
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {

            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            int count = 0, start = -1, end = -1;

            for (int i = 0; i < n; i++) {
                if (arr[i] > 0) {
                    start = i;
                    break;
                }
            }

            for (int i = 0; i < n; i++) {
                if (arr[i] > 0) {
                    end = i;
                }
            }

            if (start == -1) {
                System.out.println(0);
                continue;
            }

            for (int i = start; i <= end; i++) {
                if (arr[i] < 0) {
                    count++;
                }
            }
            System.out.println(count);

        }
    }
}
