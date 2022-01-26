#include <stdio.h>

int main() {
	int N, max, ans = 1;
	int arr[1001];
	int dp[1001];
	dp[1] = 1;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++)
		scanf("%d", &arr[i]);

	for (int i = 2; i <= N; i++) {
		max = 0;
		for (int j = 1; j < i; j++) {
			if (arr[i] > arr[j] && max < dp[j])
				max = dp[j];
		}
		dp[i] = max + 1;
		if (dp[i] > ans)
			ans = dp[i];
	}
	printf("%d", ans);
	return 0;
}
