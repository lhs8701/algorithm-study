#include<stdio.h>
long long N;

long long min(long long num1, long long num2) {
	return (num1 < num2) ? num1 : num2;
}

long long func(long long num) {
	long long sum = 0;
	for (long long i = 1; i<= N ; i++) {
		sum += min(num / i, N);
	}
	return sum;
}

long long search(long long num, long long k) {
	long long left = 1, right = num, mid;
	long long temp, ans = 1;
	while (left <= right) {
		mid = (left + right) / 2;
		temp = func(mid);
		if (temp >= k) {
			ans = mid;
			right = mid-1;
		}
		else {
			left = mid + 1;
		}
	}
	return ans;
}

int main() {
	long long k;
	scanf("%lld%*c", &N);
	scanf("%lld%*c", &k);
	printf("%lld", search(N*N, k));

	return 0;
}