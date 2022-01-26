#include <stdio.h>
#include <stdlib.h>

int makeSum(int N) {
	int r = N, sum = N;
	while (r != 0) {
		sum += r % 10;
		r /= 10;
	}
	return sum;
}

int main() {
	int N, r, digit = 0, ans;
	int flag = 0;
	scanf("%d", &N);
	
	r = N;
	while (r != 0) {
		r /= 10;
		digit++;
	}
	for (int i = N - digit * 9; i < N; i++) {
		if (i <= 0)
			continue;
		if (makeSum(i) == N) {
			flag = 1;
			ans = i;
			break;
		}
	}
	if (flag)
		printf("%d", ans);
	else
		printf("%d", 0);

	return 0;
}