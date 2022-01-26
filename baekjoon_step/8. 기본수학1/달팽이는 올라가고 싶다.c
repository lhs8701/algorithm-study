#include <stdio.h>

int main() {
	int A, B, V;

	scanf("%d %d %d", &A, &B, &V);
	double x = (double)(V - B) / (A - B);
	if ((int)x < x)
		x++;
	printf("%d", (int)x);

	return 0;
}

