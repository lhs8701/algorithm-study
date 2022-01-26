#include <stdio.h>

int main() {
	int N, K, r, cnt = 0, i;
	int unit[10];
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i++)
		scanf("%d", &unit[i]);
	r = K;
	i = N - 1;
	while (r != 0) {
		if (r >= unit[i]) {
			cnt += r / unit[i];
			r %= unit[i];
		}
		i--;
	}
	printf("%d", cnt);

	return 0;
}