package com.temp;

import java.io.*;
import java.util.*;
import java.lang.*;

public class HashMapForSequenceOfNumber {

	public static void main(String[] args) {
		int i = 1,j;
		Map<Integer, Integer> temp = new LinkedHashMap<Integer, Integer>();
		int input[] = { 5, 2, 3, 5, 8, 7, 2, 3, 8 };
		temp.put(input[0],1);
		while (i<input.length) {
			if(temp.containsKey(input[i]))
			{
				for(Map.Entry s : temp.entrySet())
				{
					if((int)s.getKey() == input[i]) {
						s.setValue((int)s.getValue() + 1);
						//System.out.println(temp.toString());
						break;
					}
				}
			}
			else {
				temp.put(input[i],1);
			//	System.out.println(temp.toString());
			}
			i++;
		}
		for (Map.Entry s : temp.entrySet())
		{
			for(j= 0 ;j<(int)s.getValue();j++)
			{
				System.out.print(s.getKey()+",");
			}
			
		}
		System.out.println(temp.toString());
	}

}
