package com.temp;

public class ClassLoader {

	public static void main(String[] args) {

		String s = new String ();
		
		Class c = ClassLoader.class;
		System.out.println(c.getClassLoader());
		
		System.out.println(String.class.getClassLoader());
	}

}
