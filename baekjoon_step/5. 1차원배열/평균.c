#include <stdio.h>
#include <stdlib.h>

int main() {

	int N, max = -1;
	int* p = NULL;
	double sum = 0;

	scanf("%d", &N);
	p = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++) {
		scanf("%d", p + i);
		if (max < p[i])
			max = p[i];
	}
	for (int i = 0; i < N; i++) {
		double temp = p[i] / (double)max * 100;
		sum += temp;
	}
	printf("%lf", sum / N);

	return 0;
}

