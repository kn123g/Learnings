
package com.temp;

public class SubArrayMaimumSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	//	int a[] = {5,-1,0,9,2,-1};
		int a[] = {-2, -5, 6, -2, -3, 1, 5, -6};
		int left=0,right=0;
		int max= a[0],i,current = 0,templeft=0;
		for (i=1;i<a.length;i++)
		{
			current = current + a[i];
			if(current<0 )
			{
				templeft = i+1;
				current=0;
			}
			if(current>max)
			{
				left = templeft;
				right = i;
				max = current ;
			}
		}
		System.out.println(max + " " +left + " " +right );
		
	}

}
