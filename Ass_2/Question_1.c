#include <stdio.h>

int main()
{
	int m;
	printf("What is your mark? ");
	scanf("%i",&m);
	if (m>40){
		printf("PASSED \n");
	}
	else{
		printf("FAILED \n");
	}

}
