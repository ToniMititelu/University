
#include <unistd.h>

int main() {
	int n = write(1, "Hello World\n", 16);
	if(n < 0) {
		return 1;
	}
	
	n = close(1);
	if(n < 0) {
		return 1;
	}

	return 0;
}
