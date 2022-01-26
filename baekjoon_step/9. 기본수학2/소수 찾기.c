#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int N, cnt = 0;
	int input[100];
	int arr[1001] = { 0, };
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &input[i]);
	}
	arr[1] = 1;
	for (int i = 2; i <= 32; i++) {
		for (int j = pow(i, 2); j <= 1000; j += i) {
			if (!arr[j])
				arr[j] = 1;
		}
	}

	for (int i = 0; i < N; i++) {
		if (!arr[input[i]])
			cnt++;
	}
	printf("%d", cnt);

	return 0;
}

