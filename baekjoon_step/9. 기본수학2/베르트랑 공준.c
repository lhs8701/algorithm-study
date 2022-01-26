#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
	
	int n,sum;
	int* num = NULL;
	num = (int*)malloc(sizeof(int) * 250000);
	while (1) {
		scanf("%d", &n);
		if (n == 0)
			break;
		memset(num, 0, sizeof(int) * 250000);
		num[1] = 1;
		sum = 0;
		for (int i = 2; i*i <= 2 * n; i++) {
			if (num[i])
				continue;
			for (int j = i*i; j <= 2 * n; j += i) {
				if (!num[j])
					num[j] = 1;
			}
		}
		for (int i = n + 1; i <= 2 * n; i++) {
			if (!num[i])
				sum++;
		}
		printf("%d\n", sum);
	}
	free(num);
	return 0;
}


