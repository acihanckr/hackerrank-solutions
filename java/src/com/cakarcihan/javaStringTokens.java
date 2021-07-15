package com.cakarcihan;

import java.util.*;

public class javaStringTokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // start
        String[] string_ar = s.split("[^A-Za-z]+",-1);
        int count = 0;
        for(String str: string_ar){
            if (!str.equals("")) count++;
        }
        System.out.println(count);
        for(String str: string_ar){
            if (!str.equals("")) System.out.println(str);
        }
        // end
        scan.close();
    }
}

