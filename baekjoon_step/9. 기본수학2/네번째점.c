#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
	int x[3];
	int y[3];
	int xnum1, xnum2, ynum1, ynum2;
	int xsum=0, ysum=0;
	for (int i = 0; i < 3; i++) {
		scanf("%d %d", &x[i], &y[i]);
		xsum += x[i];
		ysum += y[i];
	}
	xnum1 = x[0];
	ynum1 = y[0];
	for (int i = 1; i < 3; i++) {
		if (x[i] != xnum1)
			xnum2 = x[i];
		if (y[i] != ynum1)
			ynum2 = y[i];
	}
	printf("%d %d", xnum1 * 2 + xnum2 * 2 - xsum, ynum1 * 2 + ynum2 * 2 - ysum);

	return 0;
}


