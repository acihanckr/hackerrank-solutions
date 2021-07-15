package com.cakarcihan;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//Complete the classes below
//start

class Flower {
    public String whatsYourName(){
        return "I have many names and types.";
    }
}

class Jasmine extends Flower{
    @Override
    public String whatsYourName(){
        return "Jasmine";
    }
}

class Lily extends Flower{
    @Override
    public String whatsYourName(){
        return "Lily";
    }
}

class Region {
    public Flower yourNationalFlower(){
        Flower flower = new Flower();
        return flower;
    }
}

class WestBengal extends Region{
    @Override
    public Flower yourNationalFlower(){
        Jasmine jasmine = new Jasmine();
        return jasmine;
    }
}

class AndhraPradesh extends Region{
    @Override
    public Flower yourNationalFlower(){
        Lily lily = new Lily();
        return lily;
    }
}
//end

public class javaCovariantReturnTypes {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String s = reader.readLine().trim();
        Region region = null;
        switch (s) {
            case "WestBengal":
                region = new WestBengal();
                break;
            case "AndhraPradesh":
                region = new AndhraPradesh();
                break;
        }
        Flower flower = region.yourNationalFlower();
        System.out.println(flower.whatsYourName());
    }
}