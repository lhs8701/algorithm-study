#include <stdio.h>

int main() {
	int N;
	int* dp;
	scanf("%d", &N);
	dp = (int*)malloc(sizeof(int)*(N + 1));
	dp[1] = 1;
	dp[2] = 2;
	for (int i = 3; i <= N; i++) {
		dp[i] = (dp[i - 1] % 15746 + dp[i - 2] % 15746) % 15746;
	}
	printf("%d", dp[N]);

	return 0;
}