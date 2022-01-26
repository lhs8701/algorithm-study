#include <stdio.h>

void Swap(int* arr, int idx1, int idx2) {
	int temp = arr[idx1];
	arr[idx1] = arr[idx2];
	arr[idx2] = temp;
}

int partition(int* arr, int left, int right) {
	int pivot = left, low = left + 1, high = right;

	while (low <= high) {
		while (arr[pivot] <= arr[low] && low <= right)
			low++;
		while (arr[pivot] >= arr[high] && high > left)
			high--;
		if (low <= high)
			Swap(arr, low, high);
	}
	Swap(arr, high, pivot);
	return high;
}

void quickSort(int*arr, int left, int right) {
	int pivot;
	if (left <= right) {
		pivot = partition(arr, left, right);
		quickSort(arr, left, pivot - 1);
		quickSort(arr, pivot + 1, right);
	}
}

int main() {
	int N, r, idx = 0;
	int arr[10];
	scanf("%d", &N);
	r = N;
	while (r != 0) {
		arr[idx++] = r % 10;
		r /= 10;
	}
	quickSort(arr, 0, idx - 1);
	for (int i = 0; i < idx; i++)
		printf("%d", arr[i]);

	return 0;
}