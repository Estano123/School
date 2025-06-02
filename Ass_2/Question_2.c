#include <stdio.h>

float main()
{
        float m;
        printf("What is your mark? ");
        scanf("%f",&m);
        if (m<=39.9){
                printf("F \n");
        }
        else if(m>=40.0 && m<=49.9) {
                printf("C \n");
        }
	else if(m>=50 && m<=69.9){
		printf("B \n");
	}
	else{
		printf("A \n");
	}

}

