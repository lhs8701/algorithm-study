#include <stdio.h>

int facto(int N) {
	if (N == 0)
		return 1;
	return N*facto(N - 1);
}

int main() {
	int N;
	scanf("%d", &N);
	printf("%d",facto(N));

	return 0;
}


