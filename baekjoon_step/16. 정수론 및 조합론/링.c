#include<stdio.h>

int gcd(int n1, int n2) {
	int temp;
	while (n2 != 0) {
		temp = n1%n2;
		n1 = n2;
		n2 = temp;
	}
	return n1;
}

int main() {
	int N;
	int first, ring, n;
	scanf("%d%*c", &N);
	scanf("%d", &first);
	for (int i = 1; i < N; i++) {
		scanf("%d", &ring);
		n = gcd(first, ring);
		printf("%d/%d\n", first / n, ring / n);
	}
	

	return 0;
}