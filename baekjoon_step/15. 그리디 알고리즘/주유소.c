#include <stdio.h>
#include <stdlib.h>

int main() {
	int N;
	long long curPrice;
	scanf("%d%*c", &N);
	long long* gs = (long long*)malloc(sizeof(long long)*(N));
	long long* r = (long long*)malloc(sizeof(long long)*(N - 1));
	long long sum = 0;

	for (int i = 0; i < N - 1; i++)
		scanf("%lld", &r[i]);
	scanf("%*c");
	for (int i = 0; i < N; i++)
		scanf("%lld", &gs[i]);

	curPrice = gs[0];
	sum = gs[0] * r[0];
	for (int i = 1; i < N - 1; i++) {
		if (curPrice > gs[i]) 
			curPrice = gs[i];
		sum += curPrice*r[i];
	}
	printf("%lld", sum);
	free(gs);
	free(r);

	return 0;
}