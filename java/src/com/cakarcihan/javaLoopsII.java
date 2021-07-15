package com.cakarcihan;

import java.util.Scanner;

public class javaLoopsII {
    public static void main(String []argh){
        int total;
        Scanner in;
        in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            // start
            total = a+b;
            for (int j = 1; j<=n; j++){
                System.out.print(new StringBuilder().append((int) total).append(" ").toString());
                total = (int) (total + Math.pow(2, j) * b);
            }
            System.out.println();
            // end
        }
        in.close();
    }
}
