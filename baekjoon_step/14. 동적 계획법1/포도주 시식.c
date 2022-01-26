#include <stdio.h>

int Max(int num1, int num2, int num3) {
	if (num1 > num2)
		if (num1 > num3)
			return num1;
		else
			return num3;
	else
		if (num2 > num3)
			return num2;
		else
			return num3;
}

int main() {
	int N, sum = 0;
	int arr[10001];
	int dp[10001];
	int max;
	scanf("%d%*c", &N);
	for (int i = 1; i <= N; i++)
		scanf("%d%*c",&arr[i]);
	dp[0] = 0;
	dp[1] = arr[1];
	dp[2] = dp[1] + arr[2];
	for (int i = 3; i <= N; i++) {
		dp[i] = Max(dp[i - 1], dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);
	}
	printf("%d", dp[N]);
	return 0;
}
