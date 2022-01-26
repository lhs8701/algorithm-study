
/*

void Swap(int* arr, int num1, int num2) {
	int temp = arr[num1];
	arr[num1] = arr[num2];
	arr[num2] = temp;
}

void bubbleSort(int*arr, int N) {
	for (int i = 0; i < N - 1; i++) {
		for (int j = 0; j < N - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				Swap(arr, j, j + 1);
			}
		}
	}
}

void selectionSort(int*arr, int N) {
	int min;
	for (int i = 0; i < N - 1; i++) {
		min = i;
		for (int j = i + 1; j < N; j++) {
			if (arr[min] > arr[j])
				min = j;
		}
		Swap(arr, min, i);
	}
}

void insertionSort(int*arr, int N) {
	int data;
	int i, j;
	for (i = 1; i < N; i++) {
		data = arr[i];
		for (j = i - 1; j >= 0; j--) {
			if (data < arr[j])
				arr[j + 1] = arr[j];
			else
				break;
		}
		arr[j + 1] = data;
	}
}

int partition(int*arr, int left, int right) {
	int pivot = arr[left];
	int low = left + 1, high = right;

	while (low <= high) {
		while (pivot >= arr[low] && low <= right)
			low++;
		while (pivot <= arr[high] && high > left)
			high--;

		if (low <= high)
			Swap(arr, low, high);
	}
	Swap(arr, left, high);
	return high;
}

void quickSort(int*arr, int left, int right) {
	if (left <= right) {
		int pivot = partition(arr, left, right);
		quickSort(arr, left, pivot - 1);
		quickSort(arr, pivot + 1, right);
	}
}

void mergeTwoArea(int* arr, int left, int mid, int right) {
	int* sortArr = (int*)malloc(sizeof(int)*(right + 1));
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

void mergeSort(int* arr, int left, int right) {
	int mid;

	if (left < right) {
		mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);

		mergeTwoArea(arr, left, mid, right);
	}
}



*/