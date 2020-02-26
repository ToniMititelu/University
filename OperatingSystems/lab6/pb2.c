#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <pthread.h>
#include <errno.h>

#define ROW1 3
#define COL1 3
#define ROW2 3
#define COL2 3

void *mult(void* arg) 
{ 
    int *data = (int *)arg; 
    int k = 0, i; 

    for (i = 0; i < COL1; i++) 
           k += data[i]*data[i+COL1]; 
    
    int *p = (int*)malloc(sizeof(int)); 
    *p = k; 

    pthread_exit(p); 
} 

int main(int argc, char *argv[]) {

    int matrix_A[ROW1][COL1] = {
        {1, 2, 3},
        {2, 3, 4},
        {1, 3, 2}
    };

    int matrix_B[ROW2][COL2] = {
        {2, 1, 3},
        {1, 1, 1},
        {2, 0, 1}
    };

    /*
    result = {
        {10, 3, 8},
        {15, 5, 13},
        {9, 4, 8}
    }
    */

    if(COL1 != ROW2) {
        printf("not possible...\n");
        return 1;
    }

    pthread_t *threads = (pthread_t*)malloc(ROW1*COL2*sizeof(pthread_t));
    int nr_threads = 0, i, j, k;
    int *data = NULL;

    for(i=0; i<ROW1; i++) {
        for(j=0; j<COL2; j++) {
            data = (int*)malloc((COL1+ROW2)*sizeof(int));
            for(k=0; k<COL1; k++) {
                data[k] = matrix_A[i][k];
            }
            for(k=0; k<ROW2; k++) {
                data[k+COL1] = matrix_B[k][j];
            }
            
            if(pthread_create(&threads[nr_threads++], NULL, mult, data)) {
                printf("faield to create thread...\n");
                    perror(NULL);
                    return errno;
            }
        }
    }
    i = 0;
    while(i < ROW1*COL2) {
        void *k;
        if(pthread_join(threads[i], &k)) {
            printf("thread failed...\n");
            perror(NULL);
            return errno;
        }
        int *nr = (int *)k;
        printf("%d ", *nr);
        i++;
        if((i%COL2) == 0) {
            printf("\n");
        }
    }
    return 0;
}