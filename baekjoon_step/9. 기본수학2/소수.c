#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int M, N, sum = 0;
	int arr[10001] = { 0, };
	int min, flag = 0;
	scanf("%d", &M);
	scanf("%d", &N);

	arr[1] = 1;
	for (int i = 2; i <= 100; i++) {
		if (arr[i] == 1)
			continue;
		for (int j = pow(i, 2); j <= 10000; j += i) {
			if (!arr[j])
				arr[j] = 1;
		}
	}
	for (int i = M; i <= N; i++) {
		if (!arr[i]) {
			sum += i;
			if (!flag) {
				min = i;
				flag = 1;
			}
		}
	}
	if (flag)
		printf("%d\n%d", sum, min);
	else
		printf("-1");
	return 0;
}