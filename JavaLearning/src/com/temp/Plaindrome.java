package com.temp;

public class Plaindrome {

	public static void main(String[] args) {
		
		int a =101,b=0;
		int temp,temp1= a;
		while(temp1 != 0)
		{
			temp=temp1%10;
			temp1= temp1/10;
			b= (b*10)+temp;
			
		}
		if(a==b)
		{
			System.out.println("palindrome "+ a +" "+ b);
		}
		else 
		{
			System.out.println("not palindrome "+ a +" "+ b);
		}
		
		
		
	}

}
