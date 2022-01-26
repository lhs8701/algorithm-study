#include <stdio.h>

int main() {
	int T;
	int N;
	int dp[40];
	int oneCount[41];
	int zeroCount[41];
	zeroCount[0] = 1;
	zeroCount[1] = 0;
	oneCount[0] = 0;
	oneCount[1] = 1;
	scanf("%d%*c", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d%*c", &N);
		for (int j = 2; j <= N; j++) {
			zeroCount[j] = zeroCount[j - 1] + zeroCount[j - 2];
			oneCount[j] = oneCount[j - 1] + oneCount[j - 2];
		}
		printf("%d %d\n", zeroCount[N], oneCount[N]);
	}

	return 0;
}