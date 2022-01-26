#include <stdio.h>

int Max(int num1, int num2) {
	if (num1 > num2)
		return num1;
	else
		return num2;
}

int main() {
	int N;
	int arr[301];
	int dp[301][2];
	int comb[301][2];
	scanf("%d%*c", &N);
	for (int i = 1; i <= N; i++)
		scanf("%d%*c", &arr[i]);

	dp[0][0] = 0;
	dp[0][1] = 0;
	dp[1][0] = arr[1];
	dp[1][1] = arr[1];
	comb[0][0] = 0;
	comb[0][1] = 0;
	comb[1][0] = 1;
	comb[1][1] = 1;

	for (int i = 2; i <= N; i++) {
		dp[i][0] = Max(dp[i - 2][0], dp[i - 2][1]) + arr[i];
		comb[i][0] = 1;

		if (comb[i - 1][1] == 2) {
			dp[i][1] = dp[i - 1][0] + arr[i];
			comb[i][1] = 2;
		}
		else {
			if (dp[i - 1][0] > dp[i - 1][1]) {
				dp[i][1] = dp[i - 1][0] + arr[i];
				comb[i][1] = comb[i - 1][0] + 1;
			}
			else {
				dp[i][1] = dp[i - 1][1] + arr[i];
				comb[i][1] = comb[i - 1][1] + 1;
			}
		}
	}
	printf("%d", Max(dp[N][0], dp[N][1]));

	return 0;
}