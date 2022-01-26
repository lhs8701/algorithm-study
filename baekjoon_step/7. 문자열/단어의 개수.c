#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char input[1000000];
	int cnt = 0;
	gets(input);
	
	char* ptr = strtok(input, " ");
	while (ptr != NULL) {
		cnt++;
		ptr = strtok(NULL, " ");
	}
	printf("%d", cnt);
	
	return 0;
}

