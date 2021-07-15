package com.cakarcihan;

import java.util.*;

class Student{
    private int id;
    private String fname;
    private double cgpa;
    public Student(int id, String fname, double cgpa) {
        super();
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }
    public int getId() {
        return id;
    }
    public String getFname() {
        return fname;
    }
    public double getCgpa() {
        return cgpa;
    }
}

public class javaSort {
    // start
    static final Comparator<Student> CGPA_ORDER = new Comparator<Student>() {
    public int compare(Student e1, Student e2) {
        if(e1.getCgpa()>e2.getCgpa()) return -1;
        else if (e1.getCgpa()<e2.getCgpa()) return 1;
        else return 0;
    }
};
    static final Comparator<Student> NAME_ORDER = new Comparator<Student>() {
        public int compare(Student e1, Student e2) {
            return e1.getFname().compareTo(e2.getFname());
        }
    };
    // end
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());

        List<Student> studentList = new ArrayList<Student>();
        while(testCases>0){
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();

            Student st = new Student(id, fname, cgpa);
            studentList.add(st);

            testCases--;
        }
        // start
        Collections.sort(studentList, NAME_ORDER);
        Collections.sort(studentList, CGPA_ORDER);
        // end
        for(Student st: studentList){
            System.out.println(st.getFname());
        }
    }
}
