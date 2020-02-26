#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h>
#include <string.h> 
#include <errno.h>

void *threadFun(void *arg) {

    char *string1 = (char*)arg;
    int len = strlen(string1);
    char *string2 = (char*)malloc(len);
    for(int i=0; i<len; i++) {
        string2[len-i-1] = string1[i];
    }
    pthread_exit(string2);
}

int main(int argc, char *argv[]) {
    
    if(argc != 2) {
        printf("please type a word...\n");
        return 1;
    }

    pthread_t thr;
    if(pthread_create(&thr, NULL, threadFun, argv[1])) {
        printf("faield to create thread...\n");
        perror(NULL);
        return errno;
    }
    
    void *result;
    if(pthread_join(thr, &result)) {
        printf("thread failed...\n");
        perror(NULL);
        return errno;
    }
    else {
        char *string = (char *)result;
        printf("%s\n", string);
    }
    
    return 0;
}