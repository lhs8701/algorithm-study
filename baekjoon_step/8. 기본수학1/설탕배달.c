#include <stdio.h>

int main() {
	int N;
	int n, i, flag = 0;
	scanf("%d", &N);
	n = N / 5;
	for (i = n; i >= 0; i--) {
		if ((N - i * 5) % 3 == 0) {
			flag = 1;
			break;
		}
	}
	if (flag) {
		printf("%d", i + (N - i * 5) / 3);
	}
	else {
		printf("-1");
	}

	return 0;
}

