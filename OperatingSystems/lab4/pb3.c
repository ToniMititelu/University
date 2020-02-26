#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) 
    { 
        printf("arg missing\n"); 
        return 1; 
    } 
    int i;
    for(i=0; i<argc; i++) {
        if (atoi(argv[i]) < 0) 
        { 
            printf("negative number entered %d\n", atoi(argv[i])); 
            return 1; 
        } 
    }
    pid_t pid;
    int parent = getppid();
    printf("Starting parent %d\n", parent);
    for(i=1; i<argc; i++) {
        pid = fork();
        if(pid < 0) {
            printf("failed to create child\n");
            return 1;
        } 
        else if(pid == 0) {
            int n = atoi(argv[i]);
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
            printf("Done Parent %d Child %d\n", parent, getpid());
            exit(0);
        }
    }
    for(i=0; i<argc; i++) {
        wait(NULL);
    }
    return 0;
}