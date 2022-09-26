#include<stdio.h>
#include<math.h>
int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	if (a == b && b == c)
		printf("%d", 10000 + a * 1000);
	else if (a != b && b != c && a != c)
		printf("%d", ((a > b) ? ((a > c) ? a : c) : (b > c) ? b : c) * 100);
	else
		printf("%d", 1000 + ((a == b || a == c) ? a : b) * 100);
	return 0;
}