#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
	
	int M, N;
	int* num;
	num = (int*)malloc(sizeof(int) * 1000001);
	memset(num, 0, sizeof(int)*1000001);
	scanf("%d %d", &M, &N);
	num[1] = 1;
	for (int i = 2; i*i <= N; i++) {
		if (num[i])
			continue;
		for (int j = i*i; j <= N; j += i) {
			num[j] = 1;
		}
	}

	for (int i = M; i <= N; i++) {
		if (!num[i])
			printf("%d\n", i);
	}
	free(num);
	
	return 0;
}


