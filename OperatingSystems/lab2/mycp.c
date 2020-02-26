#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    int desc_1, desc_2;
    desc_1 = open(argv[1], O_RDONLY);
    if(desc_1 < 0) {
        printf("err");
        return 1;
    }
    desc_2 = open(argv[2], O_WRONLY | O_CREAT, 00644);
    if(desc_2 < 0) {
        printf("err");
        return 1;
    }
    
    struct stat sb;
    if(stat(argv[1], &sb)) {
        perror(argv[1]);
        return 1;
    }
    char *data;
    data = (char*)malloc(sb.st_size);
    if(!data) {
        return 1;
    }
    int buf_size = 2048;
    int poz = 0;
    while(poz < sb.st_size) {
        int n = read(desc_1, data, buf_size);
        write(desc_2, data, n); 
        poz += buf_size;
    }
    int a = close(desc_1);
    if(a < 0) {
        return 1;
    }
    a = close(desc_2);
    if(a < 0) {
        return 1;
    }

    free(data);

    return 0;
}