#include <stdio.h>

int min(int n1, int n2) {
	if (n1 < n2)
		return n1;
	else
		return n2;
}

int main() {
	int N;
	int dp[1001][4];
	int house[1001][4];

	scanf("%d%*c", &N);
	for (int i = 1; i <= N; i++)
		scanf("%d %d %d%*c", &house[i][1], &house[i][2], &house[i][3]);

	dp[1][1] = house[1][1];
	dp[1][2] = house[1][2];
	dp[1][3] = house[1][3];

	for (int i = 2; i <= N; i++) {
		dp[i][1] = min(dp[i - 1][2], dp[i - 1][3]) + house[i][1];
		dp[i][2] = min(dp[i - 1][1], dp[i - 1][3]) + house[i][2];
		dp[i][3] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][3];
	}
	printf("%d", min(min(dp[N][1], dp[N][2]), dp[N][3]));

	return 0;
}




