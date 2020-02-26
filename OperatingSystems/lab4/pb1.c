#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main() {
	pid_t pid = fork();
	char *parmList[3] = {"/tmp/guest-vnxeiw/SO/lab4", NULL};
	if (pid < 0) {
		return 1;
	}
	else if (pid == 0){
		execve("/bin/ls", parmList, NULL);
	}
	else {
		printf("Parent %d Child %d\n", getppid(), getpid());
		wait(NULL);
	}
	return 0;
}

