package com.cakarcihan;

import java.util.Scanner;

public class javaSubstring {

        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            String S = in.next();
            int start = in.nextInt();
            int end = in.nextInt();

            // start
            System.out.println(S.substring(start,end));
            // end
        }
}
