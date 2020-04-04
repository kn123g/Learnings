package com.temp;

import java.util.*;
import java.io.*;

public class abacbdTOabcdef {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String word;
		int i, j;
		char temp;
		String compare;
		boolean isthere;
		Scanner scan = new Scanner(System.in);
		word = scan.next();
		compare = word.charAt(0) + "";
		for (i = 1; i < word.length(); i++) {
			isthere = false;
			temp = word.charAt(i);
			for (j = 0; j < compare.length(); j++) {
				if (compare.charAt(j) == temp) {

					isthere = true;
					break;

				}

			}
			if (isthere) {
				word = word.substring(0, i) + word.substring(i, word.length()).replace(temp, (char) (temp + 1));
				compare = compare + (char) (temp + 1);
				// System.out.println("word " + word + " compare " + compare);
			} else {

				compare = compare + temp;
			}

		}
		System.out.println(word);

	}

}
