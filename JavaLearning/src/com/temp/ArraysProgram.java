package com.temp;

import java.util.Arrays;

public class ArraysProgram {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = { 50, 10, 30, 20, 40 };
		int dup[];
		Arrays.sort(arr);
		dup = Arrays.copyOf(arr, 2);
		System.out.println(Arrays.toString(dup));
	}

}
