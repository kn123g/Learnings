package com.temp;

import java.io.IOException;
import java.util.Scanner;


public class ExceptionHandling {

	public void execute()
	{
		
		int i=10;
		
		Scanner s = new Scanner(System.in);
		i=Integer.parseInt(s.next());
		System.out.println("hai");
		/*try {
			i=i/0;
		}
		catch(Exception e)
		{ 
		System.out.println(e);
		}*/
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ExceptionHandling o = new ExceptionHandling();
		o.execute();
	}

}
