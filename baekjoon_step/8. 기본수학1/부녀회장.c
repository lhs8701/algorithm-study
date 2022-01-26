#include <stdio.h>

int main() {
	int T, k, n;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d", &k);
		scanf("%d", &n);
		int apart[15][15];
		for (int i = 0; i <= n; i++)
			apart[0][i] = i;
		for (int i = 0; i <= k; i++)
			apart[i][0] = 0;

		for (int i = 1; i <= k; i++) {
			for (int j = 1; j <= n; j++) {
				apart[i][j] = apart[i][j - 1] + apart[i - 1][j];
			}
		}
		printf("%d\n", apart[k][n]);
	}

	return 0;
}

