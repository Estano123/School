#include <stdio.h>

float main()
{
	float u, t;
	printf("type Initial velocity");
	scanf("%f", &u);
	printf("Input time");
	scanf("%f", &t);
	float  a =9.8;
	float v = u + a*t;
	printf("At an acceleration of 9.8m/s, v= %f/n", v);	
}
