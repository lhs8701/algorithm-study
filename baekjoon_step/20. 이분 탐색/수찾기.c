#include<stdio.h>
#include<stdlib.h>
void mergeTwoArea(int*arr, int left, int mid, int right) {
	int*temp = (int*)malloc(sizeof(int)*(right + 1));
	int lIdx = left, rIdx = mid + 1, pIdx = left;
	while (lIdx <= mid && rIdx <= right) {
		if (arr[lIdx] < arr[rIdx])
			temp[pIdx++] = arr[lIdx++];
		else
			temp[pIdx++] = arr[rIdx++];
	}
	if (lIdx > mid) {
		while (rIdx <= right)
			temp[pIdx++] = arr[rIdx++];
	}
	else {
		while (lIdx <= mid)
			temp[pIdx++] = arr[lIdx++];
	}
	for (int i = left; i <= right; i++)
		arr[i] = temp[i];
	free(temp);
}

void mergeSort(int*arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		mergeTwoArea(arr, left, mid, right);
	}
}

int binarySearch(int*arr, int N, int key) {
	int left = 0, right = N - 1, mid;
	while (left <= right) {
		mid = (left + right) / 2;
		if (arr[mid] == key)
			return mid;
		else if (arr[mid] > key)
			right = mid - 1;
		else
			left = mid + 1;
	}
	return -1;
}

int main() {
	int N, M, idx;
	int arr[100000];
	int arr2[100000];
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);
	scanf("%d%*c", &M);
	for (int i = 0; i < M; i++)
		scanf("%d", &arr2[i]);
	mergeSort(arr, 0, N - 1);
	for (int i = 0; i < M; i++) {
		idx = binarySearch(arr, N, arr2[i]);
		if (idx == -1)
			printf("%d\n", 0);
		else
			printf("%d\n", 1);
	}
	return 0;
}