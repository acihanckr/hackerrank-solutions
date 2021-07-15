package com.cakarcihan;

import java.util.Scanner;

public class javaStdinAndStdoutI {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // start
        for (int i = 0; i<3;i++){
            int a = scan.nextInt();
            System.out.println(a);
        }
        // end
    }
}
