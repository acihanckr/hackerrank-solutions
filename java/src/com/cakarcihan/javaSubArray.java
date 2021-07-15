package com.cakarcihan;

import java.util.*;

public class javaSubArray {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] elements = new int[n];
        scan.nextLine();
        int e = 0;
        for (String elem: scan.nextLine().split(" ", -1)){
            elements[e] = Integer.parseInt(elem);
            e++;
        }
        int count = 0;
        for(int i = 0; i<n+1; i++){
            for(int j = 0; j<i; j++){
                if(Arrays.stream(Arrays.copyOfRange(elements,j,i)).sum()<0) count++;

            }
        }
        System.out.println(count);

    }
}
