#include <stdio.h>
#include <stdlib.h>

struct data {
	int num;
	int idx;
	int order;
}typedef Data;

void mergeTwoArea(Data*arr, int left, int mid, int right) {
	Data* sortArr = (Data*)malloc(sizeof(Data)*(right + 1));
	int idx1 = left, idx2 = mid + 1, sIdx = left;
	while (idx1 <= mid && idx2 <= right) {
		if (arr[idx1].num <= arr[idx2].num)
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

void mergeSort(Data*arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		mergeTwoArea(arr, left, mid, right);
	}
}

int main() {
	int N;
	Data* arr;
	Data* ans;
	int cnt = 0;
	scanf("%d%*c", &N);
	arr = (Data*)malloc(sizeof(Data)*N);
	ans = (Data*)malloc(sizeof(Data)*N);
	
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i].num);
		arr[i].idx = i;
	}
	mergeSort(arr, 0, N - 1);
	arr[0].order = 0;
	for (int i = 1; i < N; i++) {
		if (arr[i].num == arr[i - 1].num)
			cnt++;
		arr[i].order = i - cnt;
	}
	for (int i = 0; i < N; i++) 
		ans[arr[i].idx] = arr[i];
	
	for (int i = 0; i < N; i++)
		printf("%d ", ans[i].order);
	
	free(arr);
	free(ans);
	return 0;
}