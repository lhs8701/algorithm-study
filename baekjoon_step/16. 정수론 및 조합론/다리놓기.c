#include<stdio.h>
#include<stdlib.h>

int main() {
	int T, N, K;
	long long**dp;
	scanf("%d%*c", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d%d%*c", &K, &N);
		dp = (long long**)malloc(sizeof(long*)*(N + 1));
		for (int i = 0; i <= N; i++)
			dp[i] = (long long*)malloc(sizeof(long long)*(N + 1));

		for (int i = 0; i <= N; i++) {
			for (int j = 0; j <= i; j++) {
				if (j == 0 || j == i)
					dp[i][j] = 1;
				else
					dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]);
			}
		}
		printf("%lld\n", dp[N][K]);
		for (int i = 0; i <= N; i++)
			free(dp[i]);
		free(dp);
	}
	

	return 0;
}