#include <stdio.h>
#include <stdlib.h>

int main() {
	int N, M, sum, ans, min;
	int* card = NULL;
	scanf("%d %d",&N,&M);
	card = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++)
		scanf("%d", &card[i]);

	min = M + 1;
	for (int i = 0; i < N-2; i++) {
		for (int j = i + 1; j < N-1; j++) {
			for (int k = j + 1; k < N; k++) {
				sum = card[i] + card[j] + card[k];
				if (sum <= M) {
					if (min > M - sum) {
						min = M - sum;
						ans = sum;
					}
				}
			}
		}
	}
	printf("%d", ans);
	free(card);
	return 0;
}