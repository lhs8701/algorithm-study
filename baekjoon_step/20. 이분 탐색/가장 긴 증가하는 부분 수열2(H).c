#include<stdio.h>

int lowerBound(int*arr, int num, int target) {
	int left = 0, right = num + 1, mid;
	while (left < right) {
		mid = (left + right) / 2;
		if (arr[mid] < target) {
			left = mid + 1;
		}
		else {
			right = mid;
		}
	}
	return right;
}

int main() {
	int N, cnt = 1, n, idx=0;
	int* arr;
	scanf("%d%*c", &N);
	arr = (int*)malloc(sizeof(int)*(N + 1));
	scanf("%d", &arr[0]);
	for (int i = 1; i < N; i++) {
		scanf("%d", &n);
		if (arr[idx] < n) {
			arr[++idx] = n;
			cnt++;
		}
		else {
			arr[lowerBound(arr, idx, n)] = n;
		}
	}
	printf("%d", cnt);
	return 0;
}