#include <stdio.h>
#include <stdlib.h>

struct Point {
	int x;
	int y;
}typedef Point;

int WhoIsPrior(Point p1, Point p2) {
	if (p1.y > p2.y) {
		return 1;
	}
	else if (p1.y == p2.y) {
		if (p1.x > p2.x)
			return 1;
		else
			return -1;
	}
	else {
		return -1;
	}
}

void Swap(Point* arr, int idx1, int idx2) {
	Point temp = arr[idx1];
	arr[idx1] = arr[idx2];
	arr[idx2] = temp;
}

int partition(Point* arr, int left, int right) {
	Point pivot = arr[left];
	int low = left + 1, high = right;

	while (low <= high) {
		while (WhoIsPrior(pivot, arr[low]) >= 0 && low <= right)
			low++;
		while (WhoIsPrior(pivot, arr[high]) <= 0 && high > left)
			high--;
		if (low <= high)
			Swap(arr, low, high);
	}
	Swap(arr, high, left);
	return high;
}

void quickSort(Point*arr, int left, int right) {
	int pivot;
	if (left <= right) {
		pivot = partition(arr, left, right);
		quickSort(arr, left, pivot - 1);
		quickSort(arr, pivot + 1, right);
	}
}

int main() {
	int N;
	Point* arr = NULL;
	scanf("%d", &N);
	arr = (Point*)malloc(sizeof(Point)*N);

	for (int i = 0; i < N; i++)
		scanf("%d %d", &arr[i].x, &arr[i].y);

	quickSort(arr, 0, N - 1);
	for (int i = 0; i < N; i++)
		printf("%d %d\n", arr[i].x, arr[i].y);

	return 0;
}