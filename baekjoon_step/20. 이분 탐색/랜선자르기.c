#include<stdio.h>
#include<limits.h>
int K;
int lan[10000];

long long countSegment(long long digit) {
	long long cnt = 0;
	for (int i = 0; i < K; i++) {
		cnt += lan[i] / digit;
	}
	return cnt;
}

long long func(int num, int N) {
	long long left = 1, right = num;
	long long ans = -1;
	while (left <= right) {
		long long mid = (left + right) / 2;
		if (countSegment(mid) < N) {
			right = mid - 1;
		}
		else {
			if (ans < mid)
				ans = mid;
			left = mid + 1;
		}
	}
	return ans;
}
int main() {
	int N, max = -1;

	scanf("%d%d%*c", &K, &N);
	for (int i = 0; i < K; i++) {
		scanf("%d%*c", &lan[i]);
		if (max < lan[i])
			max = lan[i];
	}
	printf("%lld", func(max, N));
	return 0;
}