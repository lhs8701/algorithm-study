#include <stdio.h>

int main() {
	int T, N;
	long long dp[101];
	dp[1] = 1; dp[2] = 1; dp[3] = 1; dp[4] = 2; dp[5] = 2;
	scanf("%d%*c", &T);
	for (int j = 6; j <= 100; j++)
		dp[j] = dp[j - 5] + dp[j - 1];

	for (int i = 0; i < T; i++) {
		scanf("%d%*c", &N);
		printf("%lld\n", dp[N]);
	}

	return 0;
}