#include <stdio.h>
#include <stdlib.h>

int main() {

	int C, N;
	scanf("%d", &C);
	for (int i = 0; i < C; i++) {
		scanf("%d", &N);
		int* p = malloc(sizeof(int)*N);
		int sum = 0;
		int cnt = 0;
		for (int j = 0; j < N; j++) {
			scanf("%d", p+j);
			sum += p[j];
		}
		double aver = sum / (double)N;
		for (int j = 0; j < N; j++) {
			if (aver < p[j])
				cnt++;
		}
		printf("%.3lf%%\n", (double)cnt / N * 100);
		free(p);
	}

	return 0;
}

