package com.cakarcihan;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class javaLoops {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());
        bufferedReader.close();
        // start
        for (int i = 1; i<11;i++){
            System.out.println(String.format("%d x %d = %d", N,i,N*i ));
        }
        // end
    }
}
