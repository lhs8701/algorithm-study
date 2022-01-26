#include <stdio.h>
#include <stdlib.h>

int Max(int n1, int n2) {
	if (n1 < n2)
		return n2;
	else
		return n1;
}

int main() {
	int n;
	int** arr;
	int** dp;
	int maxVal = -1;
	scanf("%d%*c", &n);
	arr = (int**)malloc(sizeof(int*) * (n + 1));
	dp = (int**)malloc(sizeof(int*) * (n + 1));
	for (int i = 0; i <= n; i++) {
		arr[i] = (int*)malloc(sizeof(int)*(n + 1));
		dp[i] = (int*)malloc(sizeof(int)*(n + 1));
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++)
			scanf("%d", &arr[i][j]);
		scanf("%*c");
	}
	dp[1][1] = arr[1][1];
	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			if (j == 1)
				dp[i][j] = dp[i - 1][j] + arr[i][j];
			else if (j == i)
				dp[i][j] = dp[i - 1][j - 1] + arr[i][j];
			else
				dp[i][j] = Max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j];
		}
	}
	for (int i = 1; i <= n; i++) {
		if (dp[n][i] > maxVal)
			maxVal = dp[n][i];
	}
	printf("%d", maxVal);

	for (int i = 0; i <= n; i++) {
		free(arr[i]);
		free(dp[i]);
	}
	free(arr);
	free(dp);
	return 0;
}




