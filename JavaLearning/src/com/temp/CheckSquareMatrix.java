package com.temp;

public class CheckSquareMatrix {

	public static void main(String[] args) {
		int rows, cols;
		int a[][] = { { 1, 0, 0 }, { 0, 1, 0 }, { 0, 0, 1 } };

		rows = a.length;
		cols = a[0].length;
		if (rows == cols) {
			System.out.println("Matrix is square matrix");
		}

	}

}
