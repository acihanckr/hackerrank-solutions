package com.cakarcihan;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class javaPrimalityTest {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String n = bufferedReader.readLine();
        // start
        BigInteger m = new BigInteger(n);
        System.out.println(m.isProbablePrime(100) ? "prime": "not prime");
        // end
        bufferedReader.close();
    }
}
