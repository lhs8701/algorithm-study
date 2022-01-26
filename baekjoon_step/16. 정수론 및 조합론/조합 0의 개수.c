#include<stdio.h>

int getFiveCnt(long long num) {
	int cnt = 0;
	long long five = 5;
	while (five <= num) {
		cnt += num / five;
		five *= 5;
	}
	return cnt;
}
int getTwoCnt(long long num) {
	int cnt = 0;
	long long two = 2;
	while (two <= num) {
		cnt += num / two;
		two *= 2;
	}
	return cnt;
}

int min(int n1, int n2) {
	return (n1 < n2) ? n1 : n2;
}

int main() {
	long long n, m;
	int fiveCnt1 = 0, twoCnt1 = 0;
	int fiveCnt2 = 0, twoCnt2 = 0;

	scanf("%lld %lld", &n, &m);
	fiveCnt1 = getFiveCnt(n) - getFiveCnt(n - m);
	twoCnt1 = getTwoCnt(n) - getTwoCnt(n - m);
	fiveCnt2 = getFiveCnt(m);
	twoCnt2 = getTwoCnt(m);
	if (twoCnt1 == twoCnt2)
		printf("%d", 0);
	else
		printf("%d", min(fiveCnt1 - fiveCnt2, twoCnt1 - twoCnt2));

	return 0;
}