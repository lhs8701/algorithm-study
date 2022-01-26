#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct String {
	char string[51];
}typedef String;

int WhoIsPrior(char* arr1, char* arr2) {
	if (strlen(arr1) > strlen(arr2)) {
		return 1;
	}
	else if (strlen(arr1) == strlen(arr2)) {
		return strcmp(arr1, arr2);
	}
	else {
		return -1;
	}
}

void mergeTwoArea(String* arr, int left, int mid, int right) {
	String* sortArr = (String*)malloc(sizeof(String)*(right + 1));

	int idx1 = left, idx2 = mid + 1, sIdx = left;

	while (idx1 <= mid && idx2 <= right) {
		if (WhoIsPrior(arr[idx1].string, arr[idx2].string) <= 0)
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

void mergeSort(String* arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		mergeTwoArea(arr, left, mid, right);
	}
}

int main() {
	int N;
	scanf("%d%*c", &N);
	String arr[20000];

	for (int i = 0; i < N; i++) 
		scanf("%s%*c", arr[i].string);

	mergeSort(arr, 0, N - 1);
	printf("%s\n", arr[0].string);
	for (int i = 1; i < N; i++) {
		if (strcmp(arr[i - 1].string, arr[i].string) == 0)
			continue;
		printf("%s\n", arr[i].string);
	}
	
	return 0;
}




