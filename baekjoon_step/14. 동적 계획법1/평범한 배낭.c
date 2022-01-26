#include <stdio.h>
#include <stdlib.h>

int Max(int n1, int n2) {
	if (n1 < n2)
		return n2;
	else
		return n1;
}

int main() {

	int N, K;
	int arr[101][2];
	int** dp;

	scanf("%d %d%*c", &N, &K);
	dp = (int**)malloc(sizeof(int*)*(K + 1));
	for (int i = 0; i <= K; i++)
		dp[i] = (int*)malloc(sizeof(int)*(N + 1));
	for (int i = 1; i <= N; i++)
		scanf("%d %d%*c", &arr[i][0], &arr[i][1]);
	
	for (int i = 0; i <= K; i++) {
		for (int j = 0; j <= N; j++) {
			if (i == 0 || j == 0) {
				dp[i][j] = 0;
				continue;
			}
			if (i >= arr[j][0]) 
				dp[i][j] = Max(arr[j][1] + dp[i - arr[j][0]][j-1], dp[i][j - 1]);
			else
				dp[i][j] = dp[i][j - 1];
		}
	}
	printf("%d", dp[K][N]);
	for (int i = 0; i <= K; i++)
		free(dp[i]);
	free(dp);

	return 0;
}