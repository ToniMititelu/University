#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) 
    { 
        printf("arg missing or exceeding\n"); 
        return 1; 
    } 
  
    // atoi converts string to integer 
    if (atoi(argv[1]) < 0) 
    { 
        printf("negative number entered %d", atoi(argv[1])); 
        return 1; 
    } 
    pid_t pid;
    pid = fork();
    if(pid < 0) {
        printf("failed to create child\n");
        return 1;
    } 
    else if(pid == 0) {
        int n = atoi(argv[1]);
        printf("%d: %d ", n, n);
        while(n>1) {
            if(n%2 == 0) {
                n /= 2;
                printf("%d ", n);
            }
            else {
                n = 3*n + 1;
                printf("%d ", n);
            }
        }
        printf("\n");
        exit(0);
    }
    else {
        wait(NULL);
        printf("Child %d finished\n", getpid());
    }
    return 0;
}