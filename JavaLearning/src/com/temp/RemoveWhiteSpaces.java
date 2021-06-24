package com.temp;

public class RemoveWhiteSpaces {
	public static void main(String[] args) {

		String str1 = "Remove  white spaces";
		String str2 ,str3;
		str2 = str1.replaceAll("\\s+", "");
		str3 = str1.replace("\\c+", "");
		System.out.println("String : " + str1);
		System.out.println("String after removing all the white spaces : " + str2);
		
		System.out.println("String after removing the white spaces : " + str3);
	}
}
