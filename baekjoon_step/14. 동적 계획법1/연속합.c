#include <stdio.h>

int Max(int n1, int n2) {
	if (n1 < n2)
		return n2;
	else
		return n1;
}

int main() {

	int n, max = -1001;
	int arr[100001];
	int dp[100001];
	scanf("%d%*c", &n);
	for (int i = 1; i <= n; i++)
		scanf("%d", &arr[i]);
	dp[0] = 0;
	for (int i = 1; i <= n; i++) 
		dp[i] = Max(arr[i], dp[i - 1] + arr[i]);
	
	for (int i = 1; i <= n; i++) {
		if (max < dp[i])
			max = dp[i];
	}
	printf("%d", max);
	return 0;
}