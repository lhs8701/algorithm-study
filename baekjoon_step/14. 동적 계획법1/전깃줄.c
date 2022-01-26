#include <stdio.h>

int main() {
	int N, n1, n2, maxNum = -1, result = -1, maxIdx;
	int arr[501] = { 0, };
	int dp[501] = { 0, };
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d %d%*c", &n1, &n2);
		arr[n1] = n2;
		if (maxNum < n1)
			maxNum = n1;
	}
	
	for (int i = 1; i <= maxNum; i++) {
		if (!arr[i]) 
			continue;
		maxIdx = 0;
		for (int j = 1; j < i; j++) {
			if (arr[i] > arr[j] && dp[j] > dp[maxIdx])
				maxIdx = j;
		}
		dp[i] = dp[maxIdx] + 1;
		if (result < dp[i])
			result = dp[i];
	}
	
	printf("%d", N - result);
	return 0;
}