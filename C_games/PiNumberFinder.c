//program will go through digits of pi and find a certain combination of numbers
//π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14)
#include <stdio.h>

//int find(int index, double &pie);

int main(void)
{
	double pie = 3;
	for (unsigned int i = 2, tries = 655; i < tries; i += 2)//max size of int 4,294,967,295
	{																										//for some reason tries has to not be that hi or will cause 
		if (i%4 != 0){																		//errors for the calculation even if below int max value
			pie = pie + (4.0/(i * (i + 1) * (i + 2)));
		}
		else{
			pie = pie - (4.0/(i * (i + 1) * (i + 2)));
		}
		
	}
	printf("%.50f", pie);
	return 0;
}

#if 0
int find(int index)
{
	
	return 0;
}
#endif
