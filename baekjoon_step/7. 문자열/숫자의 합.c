#include <stdio.h>
#include <stdlib.h>


int main() {
	int N, sum=0;
	scanf("%d", &N);
	char* str = malloc(sizeof(char)*N);
	scanf("%s", str);
	for (int i = 0; i < N; i++) {
		sum += (str[i] - '0');
	}
	printf("%d", sum);
	return 0;
}

