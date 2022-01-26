#include <stdio.h>

int main() {
	int X;
	scanf("%d", &X);
	int e = 0, s, i = 0;
	int sign = -1;
	while (X>e) {
		sign *= -1;
		i++;
		e += i;
	}
	s = e - i + 1;
	int numer = i + 1 - X + s - 1;
	int denom = X - s + 1;
	if (sign == 1)
		printf("%d/%d", numer, denom);
	else
		printf("%d/%d", denom, numer);
	return 0;
}

