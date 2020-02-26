#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h>
#include <string.h> 
#include <errno.h>
#include <time.h>

#define MAXRESOURCES 5
int resources = MAXRESOURCES;
pthread_t threads[MAXRESOURCES];
pthread_mutex_t mtx;

int decrease_count(int arg)
{
    while(resources < arg);
    pthread_mutex_lock(&mtx);
    resources -= arg;
    printf("Got %d resources, %d remaining\n", arg, resources);
    pthread_mutex_unlock(&mtx);
    return 0;
}

int increase_count(int arg)
{
    pthread_mutex_lock(&mtx);
    resources += arg;
    printf("Released %d resources, %d remaining\n", arg, resources);
    pthread_mutex_unlock(&mtx);
    return 0;
}

void *threadFun(void *arg)
{
    int *count = (int *)arg;
    decrease_count(*count);
    increase_count(*count);
    return NULL;
}

int main()
{
    if(pthread_mutex_init(&mtx, NULL))
    {
        perror(NULL);
        return errno;
    }

    int argc = 5;
    int *args = (int *)malloc(argc * sizeof(int));
    srand(time(0));

    for(int i=0; i<argc; i++)
    {
        args[i] = rand() % MAXRESOURCES + 1;
        if(pthread_create(&threads[i], NULL, threadFun, (void *)&args[i]))
        {
            perror(NULL);
            return errno;
        }
    }

    for(int i=0; i<argc; i++)
    {
        if(pthread_join(threads[i], NULL)) {
            printf("thread failed...\n");
            perror(NULL);
            return errno;
        }
    }

    pthread_mutex_destroy(&mtx);
    return 0;
}