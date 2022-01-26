
#include <stdio.h>
#include <stdlib.h>

typedef struct Time {
	int start;
	int end;
}Time;

int compare(Time*arr, int n1, int n2) {
	if (arr[n1].end < arr[n2].end)
		return -1;
	else if (arr[n1].end == arr[n2].end) {
		if (arr[n1].start < arr[n2].start)
			return -1;
		else
			return 1;
	}
	else
		return 1;
}
void mergeTwoArea(Time* arr, int left, int mid, int right) {
	Time* sortArr = (Time*)malloc(sizeof(Time)*(right + 1));
	int idx1 = left, idx2 = mid + 1, sIdx = left;

	while (idx1 <= mid && idx2 <= right) {
		if (compare(arr, idx1, idx2) < 0)
			sortArr[sIdx++] = arr[idx1++];
		else
			sortArr[sIdx++] = arr[idx2++];
	}
	if (idx1 > mid) {
		while (idx2 <= right)
			sortArr[sIdx++] = arr[idx2++];
	}
	else {
		while (idx1 <= mid)
			sortArr[sIdx++] = arr[idx1++];
	}

	for (int i = left; i <= right; i++)
		arr[i] = sortArr[i];

	free(sortArr);
}

void mergeSort(Time* arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		mergeTwoArea(arr, left, mid, right);
	}
}

int main() {
	int N, max, idx = 0, result = 0;
	scanf("%d", &N);
	Time* arr = (Time*)malloc(sizeof(Time)*(N + 1));
	int* dp = (int*)malloc(sizeof(int)*(N + 1));
	for (int i = 1; i <= N; i++)
		scanf("%d%d", &arr[i].start, &arr[i].end);

	mergeSort(arr, 1, N);
	dp[0] = 0;
	for (int i = 1; i <= N; i++) {
		if (arr[idx].end <= arr[i].start) {
			idx = i;
			result++;
		}
	}
	printf("%d", result);
	free(arr);
	free(dp);

	return 0;
}