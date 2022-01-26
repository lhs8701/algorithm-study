#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int Max(int num1, int num2) {
	if (num1 > num2)
		return num1;
	else
		return num2;
}

int main() {
	int** dp;
	char str1[1001];
	char str2[1001];
	int n1, n2;
	dp = (int**)malloc(sizeof(int*) * 1001);
	for (int i = 0; i < 1001; i++)
		dp[i] = (int*)malloc(sizeof(int) * 1001);
	scanf("%s%*c", str2);
	scanf("%s%*c", str1);
	n1 = strlen(str1);
	n2 = strlen(str2);
	for (int i = 0; i <= n1; i++) 
		dp[i][0] = 0;
	for (int i = 0; i <= n2; i++)
		dp[0][i] = 0;

	for (int i = 0; i < n1; i++) {
		for (int j = 0; j < n2; j++) {
			if (str1[i] == str2[j])
				dp[i+1][j+1] = dp[i][j] + 1;
			else
				dp[i+1][j+1] = Max(dp[i+1][j], dp[i][j+1]);
		}
	}
	printf("%d", dp[n1][n2]);
	for (int i = 0; i < 1001; i++)
		free(dp[i]);
	free(dp);

	return 0;
}