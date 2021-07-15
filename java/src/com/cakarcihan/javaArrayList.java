package com.cakarcihan;

import java.util.*;

public class javaArrayList {

    public static void main(String[] args) {
        //start
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.nextLine();
        List<Integer>[] alg = new ArrayList[n];

        for (int i = 0; i<n; i++){
            alg[i] = new ArrayList<Integer>();
        }
        for (int i=0; i<n; i++){
            String[] line = scan.nextLine().split(" ",-1);
            int m = Integer.parseInt(line[0]);
            for (int j=1; j<m+1; j++){
                alg[i].add(Integer.parseInt(line[j]));
            }
        }
        int o = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i<o; i++){
            String[] line = scan.nextLine().split(" ",-1);
            try {
                System.out.println(alg[Integer.parseInt(line[0])-1].get(Integer.parseInt(line[1])-1));
            } catch(IndexOutOfBoundsException e){
                System.out.println("ERROR!");

            }
        }
        // end

    }
}
