package com.cakarcihan;

import java.io.*;
import java.util.*;

public class java2DArray {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < 6; i++) {
            String[] arrRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> arrRowItems = new ArrayList<>();

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowTempItems[j]);
                arrRowItems.add(arrItem);
            }

            arr.add(arrRowItems);
        }

        bufferedReader.close();
        // start
        int largest = arr.get(0).subList(0,3).stream().mapToInt(Integer::intValue).sum()+arr.get(2).subList(0,3).stream().mapToInt(Integer::intValue).sum()+arr.get(1).get(1);
        for (int i = 0; i<arr.size()-2; i++){
            for (int j = 0; j<arr.get(0).size()-2; j++){
                int glass = arr.get(i).subList(j,j+3).stream().mapToInt(Integer::intValue).sum()+arr.get(i+2).subList(j,j+3).stream().mapToInt(Integer::intValue).sum()+arr.get(i+1).get(j+1);
                if (glass>largest) largest = glass;
            }
        }
        System.out.println(largest);
        // end
    }
}
