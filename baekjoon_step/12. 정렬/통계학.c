#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void mergeTwoArea(int*arr, int left, int mid, int right) {
	int*sortArr = (int*)malloc(sizeof(int)*(right + 1));
	int idx1 = left, idx2 = mid + 1, sIdx = left;
	while (idx1 <= mid && idx2 <= right) {
		if (arr[idx1] < arr[idx2])
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

void mergeSort(int*arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		mergeTwoArea(arr, left, mid, right);
	}
}

int main() {
	int N, min = 4001, max = -4001, maxCount = -1;
	int pNum[4001] = { 0, };
	int mNum[4001] = { 0, };
	int*arr = NULL;
	double sum = 0;
	int flag = 0, ans;
	scanf("%d", &N);
	arr = (int*)malloc(sizeof(int)*N);

	for (int i = 0; i < N; i++) {
		scanf("%d%*c", &arr[i]);
		sum += arr[i];
		if (arr[i] >= 0)
			pNum[arr[i]]++;
		else
			mNum[arr[i] * -1]++;
		if (min > arr[i])
			min = arr[i];
		if (max < arr[i])
			max = arr[i];
	}
	mergeSort(arr, 0, N - 1);

	for (int i = 4000; i > 0; i--) {
		if (mNum[i] == 0)
			continue;
		if (maxCount < mNum[i]) {
			maxCount = mNum[i];
			flag = 0;
			ans = i*-1;
		}
		else if (maxCount == mNum[i]) {
			if (flag == 0) {
				flag = 1;
				ans = i*-1;
			}
		}
	}
	for (int i = 0; i < 4001; i++) {
		if (pNum[i] == 0)
			continue;
		if (maxCount < pNum[i]) {
			maxCount = pNum[i];
			flag = 0;
			ans = i;
		}
		else if (maxCount == pNum[i]) {
			if (flag == 0) {
				flag = 1;
				ans = i;
			}
		}
	}
	printf("%.0lf\n", sum / N);
	printf("%d\n", arr[N / 2]);
	printf("%d\n", ans);
	printf("%d\n", max - min);
	return 0;
}