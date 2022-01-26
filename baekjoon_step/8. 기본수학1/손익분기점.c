#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);
	if (B >= C)
		printf("-1");
	else {
		double x = (double)A / (C - B);
		printf("%d", (int)x + 1);
	}
	return 0;
}

