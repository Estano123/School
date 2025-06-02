#include <stdio.h>

float main()
{
        float P, R, T;
        printf("Input Principal");
        scanf("%f", &P);
        printf("Input Rate");
        scanf("%f", &R);
	printf("input Number of years");
	scanf("%f", &T);

        float SI = (P*R*T)/100;
        printf("Interest = %f/n", SI);

}
