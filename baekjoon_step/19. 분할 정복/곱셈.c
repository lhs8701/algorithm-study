#include<stdio.h>
long long C;
long long power(long long a, long long b) {
	for (int i = 0; i < b-1; i++)
		a *= a;
	return a;
}
long long func(long long A, long long B) {
	if (B == 0)
		return 1;
	if (B % 2 == 0) {
		return (power(func(A, B / 2), 2)) % C;
	}
	else 
		return ((power(func(A, B / 2),2)) % C * A) % C;
}

int main() {
	long long A, B;
	scanf("%lld%lld%lld", &A, &B, &C);

	printf("%lld", func(A,B));

	return 0;
}