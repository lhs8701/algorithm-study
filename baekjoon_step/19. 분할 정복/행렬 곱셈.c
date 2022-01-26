#include<stdio.h>

int main() {
	int N, M, K, sum;
	int A[100][100];
	int B[100][100];
	scanf("%d%d%*c", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			scanf("%d", &A[i][j]);
		scanf("%*c");
	}
	scanf("%d%d%*c", &M, &K);
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < K; j++)
			scanf("%d", &B[i][j]);
		scanf("%*c");
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K; j++) {
			sum = 0;
			for (int l = 0; l < M; l++) {
				sum += A[i][l] * B[l][j];
			}
			printf("%d ", sum);
		}
		printf("\n");
	}
	return 0;
}