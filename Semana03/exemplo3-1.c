#include <stdio.h>
#include <unistd.h>

int main ()
{
	printf("O ID do processo eh %d\n", (int) getpid ());
	printf("O ID do processo parente eh %d\n", (int) getppid ());
	return 0;
}