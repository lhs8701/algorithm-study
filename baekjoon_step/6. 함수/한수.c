#include <stdio.h>
#include <stdlib.h>

int func(int num) {
	int r = num;
	int arr[4] = { 0, };
	int idx = 0;
	while (r != 0) {
		arr[idx] = r % 10;
		r /= 10;
		idx++;
	}
	int d = arr[0] - arr[1];
	for (int i = 0; i < idx-1; i++) {
		if (arr[i] - arr[i + 1] != d)
			return 0;
	}
	return 1;
}

int main() {
	int N, cnt = 0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		if (func(i))
			cnt++;
	}
	printf("%d", cnt);
}

