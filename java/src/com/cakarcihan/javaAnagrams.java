package com.cakarcihan;

import java.util.Scanner;

public class javaAnagrams {
    // start
    static int countOf(String s, char c){
        int count = 0;
        int index = 0;
        while(index<s.length()){
            if (s.indexOf(c, index) != -1){
                count++;
                index = s.indexOf(c, index)+1;
            } else{
                break;
            }

        }
        return count;
    }


    static boolean isAnagram(String a, String b) {
        boolean an = true;
        a = a.toLowerCase();
        b = b.toLowerCase();
        for (char c: a.toCharArray()){
            if (countOf(a,c) != countOf(b,c)){
                an = false;
            }
        }
        for (char c: b.toCharArray()){
            if (countOf(a,c) != countOf(b,c)){
                an = false;
            }

        }
        return an;
    }
    // end
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }

}