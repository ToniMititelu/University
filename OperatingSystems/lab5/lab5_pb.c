#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mman.h>
#include <fcntl.h> 
#include <sys/stat.h>
#include <errno.h>
#include <string.h>

int main(int argc, char *argv[]) {

    if(argc < 2) {
        printf("enter at least 1 number...\n");
        return 1;
    }
    
    pid_t parent = getpid();
    printf("Starting parent %d\n", parent);
    int shm_fd;
    char *shm_name = "collatz";

    shm_fd = shm_open(shm_name, O_CREAT|O_RDWR, S_IRUSR|S_IWUSR);
    if(shm_fd < 0) {
        perror(NULL);
        return errno;
    }

    int shm_size = getpagesize()*(argc-1);
    if(ftruncate(shm_fd, shm_size) < 0) {
        perror(NULL);
        shm_unlink(shm_name);
        return errno;
    }

    for(int i=1; i<argc; i++) {
        pid_t pid = fork();
        if(pid < 0) {
            return errno;
        }
        else if(pid == 0) {
            char *shm_ptr = mmap(0, getpagesize(), PROT_WRITE, MAP_SHARED, shm_fd, (i-1)*getpagesize());
            if(shm_ptr == MAP_FAILED) {
                perror(NULL);
                shm_unlink(shm_name);
                return errno;
            }
            int n = atoi(argv[i]);
            int written = sprintf(shm_ptr, "%d: ", n);
            shm_ptr += written;
            while(n>1) {
                written = sprintf(shm_ptr, "%d ", n);
                shm_ptr += written;
                if(n%2 == 0) {
                    n /= 2;
                }
                else {
                    n = 3*n + 1;
                }
            }

            sprintf(shm_ptr, "%d ", n);

            printf("Done Parent %d Child %d\n", parent, getpid());

            exit(0);
        }

    }

    if(getpid() == parent) {
        for(int i=0; i<argc; i++) {
            wait(NULL);
        }
        for(int i=0; i<argc-1; i++) {
            char *shm_ptr = mmap(0, getpagesize(), PROT_READ, MAP_SHARED, shm_fd, i*getpagesize());
			if(shm_ptr == MAP_FAILED)
			{
				perror(NULL);
				shm_unlink(shm_name);
				return errno;
			}
			printf("%s\n", shm_ptr);
            if(munmap(shm_ptr, 1000) == -1) {
                perror(NULL);
                return errno;
            } 
        }
    }

    return 0;
}