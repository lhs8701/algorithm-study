#include<stdio.h>
#include<stdlib.h>

int main() {
	int N, K;
	int**dp;
	scanf("%d%d", &N, &K);
	dp = (int**)malloc(sizeof(int*)*(N + 1));
	for (int i = 0; i <= N; i++)
		dp[i] = (int*)malloc(sizeof(int)*(N + 1));

	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0 || j == i)
				dp[i][j] = 1;
			else
				dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007;
		}
	}
	printf("%d", dp[N][K]);
	for (int i = 0; i <= N; i++)
		free(dp[i]);
	free(dp);

	return 0;
}