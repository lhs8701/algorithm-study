#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int T;
	double d;
	int x1, y1, r1, x2, y2, r2;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		d = sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
		if (d == 0 && r1 == r2)
			printf("-1");
		else if (d <= abs(r1 - r2)) {
			if (d == abs(r1 - r2))
				printf("1");
			else if (d < abs(r1 - r2))
				printf("0");
		}
		else {
			if (d < r1 + r2)
				printf("2");
			else if (d == r1 + r2)
				printf("1");
			else
				printf("0");
		}
		printf("\n");
	}


	return 0;
}


