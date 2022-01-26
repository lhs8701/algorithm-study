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
	int cnt = 0;
	int l, r;
	while (left <= right) {
		mid = (left + right) / 2;
		if (arr[mid] == key) {


		}
		else if (arr[mid] > key) {

		}
		else {

		}

	}
	return 0;
}

int upperBound(int* arr, int N, int key) {
	int left = 0, right = N, mid;
	while (left < right) {
		mid = (left + right) / 2;
		if (arr[mid] > key)
			right = mid;
		else
			left = mid + 1;
	}
	return right;
}

int lowerBound(int* arr, int N, int key) {
	int left = 0, right = N, mid;
	while (left < right) {
		mid = (left + right) / 2;
		if (arr[mid] >= key)
			right = mid;
		else
			left = mid + 1;
	}
	return right;
}

int main() {
	int N, M;
	scanf("%d%*c", &N);
	int* arr = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	scanf("%d%*c", &M);
	int* arr2 = (int*)malloc(sizeof(int)*M);
	for (int i = 0; i < M; i++)
		scanf("%d", &arr2[i]);
	mergeSort(arr, 0, N - 1);
	for (int i = 0; i < M; i++) {
		printf("%d ", upperBound(arr, N, arr2[i]) - lowerBound(arr, N, arr2[i]));
	}

	return 0;
}