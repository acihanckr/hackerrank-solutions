package com.cakarcihan;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class javaEndOfFile {
    // start
    static List<String> inputs = new ArrayList<>();
    static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        while (scan.hasNext()){
            inputs.add(scan.nextLine());
        }
        int count = 1;
        for (String s: inputs){
            System.out.println(count + " " + s);
            count++;
        }
    }
    // end
}
