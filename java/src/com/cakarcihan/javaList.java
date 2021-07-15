package com.cakarcihan;

import java.util.*;

public class javaList {

    public static void main(String[] args) {
        // start
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        scan.nextLine();
        String[] line = scan.nextLine().split(" ", -1);
        List<Integer> lst = new ArrayList<>();
        for (int i = 0; i<n; i++){
            lst.add(Integer.parseInt(line[i]));
        }
        int m = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i<m; i++){
            String command = scan.nextLine();
            if (command.equals("Insert")){
                line = scan.nextLine().split(" ", -1);
                lst.add(Integer.parseInt(line[0]), Integer.parseInt(line[1]));
            }
            if (command.equals("Delete")){
                lst.remove(Integer.parseInt(scan.nextLine()));
            }
        }
        String output = "";
        int o = lst.size();
        for(int i=0; i<o;i++){
            output += lst.get(i);
            if (i == o) continue;
            output += " ";
        }
        System.out.println(output);
        // end
    }
}

