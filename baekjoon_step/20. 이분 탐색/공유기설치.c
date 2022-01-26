#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
int N, C;

void mergeTwoArea(long long*arr, int left, int mid, int right) {
	long long* temp = (long long*)malloc(sizeof(long long)*(right + 1));
	int idx1 = left, idx2 = mid + 1, tIdx = left;

	while (idx1 <= mid && idx2 <= right) {
		if (arr[idx1] < arr[idx2]) 
			temp[tIdx++] = arr[idx1++];
		else
			temp[tIdx++] = arr[idx2++];
	}

	if (idx1 > mid) {
		while (idx2 <= right) 
			temp[tIdx++] = arr[idx2++];
	}
	else {
		while (idx1 <= mid)
			temp[tIdx++] = arr[idx1++];
	}

	for (int i = left; i <= right; i++)
		arr[i] = temp[i];
	free(temp);
}

void mergeSort(long long* arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid+1, right);
		mergeTwoArea(arr, left, mid, right);
	}
}

int isPossible(long long arr[], long long dis) {
	int cnt = C - 1, point = 0;
	for (int i = 1; i < N; i++) {
		if (cnt == 0)
			break;
		if (arr[i] - arr[point] >= dis) {
			cnt--;
			point = i;
		}
	}
	if (cnt)
		return 0;
	else
		return 1;
}

long long func(long long arr[], long long num) {
	long long left = 1, right = num;
	long long ans = 0;
	while (left <= right) {
		long long mid = (left + right) / 2;
		if (isPossible(arr,mid)) {
			if (ans < mid)
				ans = mid;
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}
	return ans;
}

int main() {
	long long* arr;
	scanf("%d%d%*c", &N, &C);
	arr = (long long*)malloc(sizeof(long long)*N);
	for (int i = 0; i < N; i++) 
		scanf("%lld%*c", &arr[i]);
	
	mergeSort(arr, 0, N-1);
	printf("%lld", func(arr, arr[N - 1] - arr[0]));

	return 0;
}