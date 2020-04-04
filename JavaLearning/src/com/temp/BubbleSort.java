package com.temp;

public class BubbleSort {

	public static void main(String[] args) {

		int a[] = { 8, 1, 5, 0, 9, 3 }, temp, j;
		for (int i = 0; i < a.length; i++) {
			for (j = 0; j < a.length - 1; j++) {
				if (a[j] > a[j + 1]) {
					temp = a[j];
					a[j] = a[j + 1];
					a[j + 1] = temp;
				}

			}

		}
		j = 0;
		while (j < a.length) {
			System.out.print(a[j] + " ");
			j++;
		}
	}
}
