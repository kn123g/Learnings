package com.temp;
public class SwapWithoutTemp {

	public static void main(String[] args) {
        int a=1,b=2;
        System.out.println("before swap a: " + a + " b: " +b );
        a=a+b;
        b=a-b;
        a=a-b;
        System.out.println("after swap a: " + a + " b: " +b );
    }

}