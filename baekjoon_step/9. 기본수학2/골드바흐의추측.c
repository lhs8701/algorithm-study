#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
	
	int i,j,n,T;
	int* num = NULL;
	int half;
	num = (int*)malloc(sizeof(int) * 10001);
	memset(num, 0, sizeof(int) * 10001);
	num[1] = 0;

	for (i = 2; i*i <= 10000; i++) {
		if (num[i])
			continue;
		for (j = i*i; j <= 10000; j += i) {
			if (!num[j])
				num[j] = 1;
		}
	}

	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d", &n);
		half = n / 2;
		for (i = 0; i < n-1; i++) {
			if (!num[half - i] && !num[half + i])
				break;
		}
		printf("%d %d\n", half - i, half + i);
	}

	return 0;
}


