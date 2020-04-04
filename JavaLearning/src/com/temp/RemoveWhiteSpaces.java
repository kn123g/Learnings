package com.temp;

public class RemoveWhiteSpaces {
	public static void main(String[] args) {

		String str1 = "Remove  white spaces";
		String str2 ;
		str1 = str1.replaceAll("\\s+", "");
		str2 = str1.replace("\\s+", "");
		System.out.println("String after removing all the white spaces : " + str1);
		
		System.out.println("String after removing the white spaces : " + str1);
	}
}
