package com.temp;

public class MaxRectangularSumInArray {

	public static void main(String[] args) {
		/*
		 * int a[][] = { { 1, 0, 4 }, { 5, 4, 0 }, { 1, -4, -2 } };
		 */
		int a[][] = { { 1, 		2, 		-1, 	-4, 	-20 },
						{ -8, 	-3, 	4, 		2, 		1 },
						{ 3, 	8, 		10, 	1, 		3 }, 
						{ -4, 	-1,		 1, 	7, 		-6 } };
		// System.out.println(a.length);
		int temp[] = new int[a.length];
		int maxsum = 0, maxleft = 0, maxright = 0, maxtop = 0, maxbottom = 0, top = 0, bottom = 0;

	

		int i = 0, current,temptop, max;
		maxleft = 0;
		maxright = 0;

		for (int l = 0; l < a[0].length; l++) {
			
			for (int t = 0; t < a.length; t++) {
				temp[t] = 0;
			}

			for (int o = l; o < a[0].length; o++) {

				for (int j = 0; j < a.length; j++) {
					temp[j] = temp[j] + a[j][o];
				}
				//System.out.println(temp[0] + " " + temp[1]+ " "+ temp[2]+ " "+temp[3]);
				current = 0;
				max = temp[0];
				top= 0 ;
				bottom= 0 ;
				temptop=0;
				for (int k = 0; k < temp.length; k++) {

					current = current + temp[k];
					if (current < 0) {
						
						temptop = k+1;
						current = 0;
					}
					if (current > max) {
						top = temptop;
						bottom = k;
						max = current;
					}

				}
				if (max > maxsum) {
					maxsum = max;
					maxtop = top;
					maxbottom = bottom;
					maxleft = l;
					maxright = o;
					
					

				}
				System.out.println(maxsum + "   " + maxtop + "  " + "  "+maxbottom + "  "+ maxleft +"  " + maxright);
			}

		}
		System.out.println("maxsum : " + maxsum);
		System.out.println("maxtop : " + maxtop);
		System.out.println("maxbottom : " + maxbottom);
		System.out.println("maxleft : " + maxleft);
		System.out.println("maxright : " + maxright);
	}
}
