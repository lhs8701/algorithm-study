#include <stdio.h>


int main() {
	int N, X,num;
	scanf("%d %d", &N, &X);
	for (int i = 0; i < N; i++) {
		scanf("%d", &num);
		if (num < X)
			printf("%d ", num);
	}
	return 0;
}

