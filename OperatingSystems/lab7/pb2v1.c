#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <errno.h>
#include <stdlib.h>

#define N 5
pthread_t threads[N];
pthread_mutex_t mtx;
sem_t barrier;
int count;

void barrier_point()
{
    pthread_mutex_lock(&mtx);
    count++;
    

    if(count == N)
    {
        while(count>0)
        {
            sem_post(&barrier);
            count--;
        }
    }
    pthread_mutex_unlock(&mtx);
    sem_wait(&barrier);
}

void *threadFun(void *arg)
{
    int *tid = (int *)arg;
    printf("%d reached the barrier\n", *tid);
    barrier_point();
    printf("%d passed the barrier\n", *tid);
    
    return NULL;
}

int main()
{
    if(pthread_mutex_init(&mtx, NULL))
    {
        perror(NULL);
        return errno;
    }

    if(sem_init(&barrier, 0, 0))
    {
        perror(NULL);
        return errno;
    }

    int *args = (int*)malloc(N*sizeof(int));

    for(int i=0; i<N; i++)
    {
        args[i] = i;
        if(pthread_create(&threads[i], NULL, threadFun, (void *)&args[i]))
        {
            perror(NULL);
            return errno;
        }
    }

    for(int i=0; i<N; i++)
    {
        if(pthread_join(threads[i], NULL))
        {
            perror(NULL);
            return errno;
        }
    }

    return 0;
}