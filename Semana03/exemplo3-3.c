#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main ()
{
	pid_t child_pid;

	printf("O ID do processo do programa main eh %d\n", (int) getpid ());

	child_pid = fork ();
	if (child_pid != 0) {
		printf("Esse eh o processo parente, com ID %d\n", (int) getpid ());
		printf("O ID do processo filho eh %d\n", (int) child_pid);
	}
	else
		printf("Esse eh o processo filho, com ID %d\n", (int) getpid ());

	return 0;
}