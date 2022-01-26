#include <stdio.h>

int main() {
	int w[51][51][51];
	w[0][0][0] = 1;
	while (1) {
		int a, b, c;
		scanf("%d %d %d%*c", &a, &b, &c);
		if (a == -1 && b == -1 && c == -1)
			break;
		printf("w(%d, %d, %d) = ", a, b, c);
		if (a <= 0 || b <= 0 || c <= 0) {
			a = 0; b = 0; c = 0;
		}
		else if (a > 20 || b > 20 || c > 20) {
			a = 20; b = 20; c = 20;
		}
		for (int i = 0; i <= a; i++) {
			for (int j = 0; j <= b; j++) {
				for (int k = 0; k <= c; k++) {
					if (i == 0 || j == 0 || k == 0) 
						w[i][j][k] = 1;
					else if (i < j && j < k) 
						w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k];
					else 
						w[i][j][k] = w[i - 1][j][k] - w[i - 1][j - 1][k - 1] + w[i - 1][j - 1][k] + w[i - 1][j][k - 1];
					
				}
			}
		}
		printf("%d\n",w[a][b][c]); 
	}

	return 0;
}