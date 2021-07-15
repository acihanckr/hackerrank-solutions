package com.cakarcihan;

import java.util.Scanner;
import java.util.regex.Pattern;

public class patternSyntaxChecker {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while(testCases>0){
            String pattern = in.nextLine();
            // start
            try{
                Pattern pattern_re = Pattern.compile(pattern);
                System.out.println("Valid");
            } catch(Exception e){
                System.out.println("Invalid");
            } finally{
                testCases--;
            }
            // end
        }
    }
}
