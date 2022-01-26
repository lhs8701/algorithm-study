#include<stdio.h>
#include<stdlib.h>

typedef struct Heap {
	int arr[100001];
	int num;
	int(*comp)(int, int);
}Heap;

int compMIN(int num1, int num2) {
	if (num1 < num2)
		return 1;
	else
		return -1;
}

int compMAX(int num1, int num2) {
	if (num1 < num2)
		return -1;
	else
		return 1;
}

void HeapInit(Heap* ph, int num) {
	ph->num = 0;
	if (num == 0)
		ph->comp = compMIN;
	else
		ph->comp = compMAX;
}

int HIsEmpty(Heap* ph) {
	if (ph->num == 0)
		return 1;
	else
		return 0;
}

void HInsert(Heap* ph, int data) {
	int idx = ++ph->num;
	while (idx != 1 && ph->comp(ph->arr[idx / 2], data)<0) {
		ph->arr[idx] = ph->arr[idx / 2];
		idx /= 2;
	}
	ph->arr[idx] = data;
}

int getPriorChild(Heap* ph, int idx) {
	if (idx * 2 > ph->num) {
		return 0;
	}
	else if (idx * 2 == ph->num) {
		return idx * 2;
	}
	else {
		return (ph->comp(ph->arr[idx * 2], ph->arr[idx * 2 + 1])<0) ? idx * 2 + 1 : idx * 2;
	}
}

int HDelete(Heap* ph) {
	int parent = 1, child;
	int lastElem = ph->arr[ph->num--];
	int RData = ph->arr[1];

	while (child = getPriorChild(ph, parent)) {
		if (ph->comp(lastElem, ph->arr[child])>0)
			break;
		ph->arr[parent] = ph->arr[child];
		parent = child;
	}
	ph->arr[parent] = lastElem;
	return RData;
}

int main() {
	int N, n, mid, temp1, temp2;
	Heap maxHeap;
	Heap minHeap;
	HeapInit(&maxHeap,1);
	HeapInit(&minHeap,0);
	scanf("%d%*c", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d%*c", &n);
		if (i % 2 == 1) 
			HInsert(&maxHeap, n);
		else 
			HInsert(&minHeap, n);

		if (maxHeap.num && minHeap.num && maxHeap.arr[1] > minHeap.arr[1]) {
			temp1 = HDelete(&maxHeap);
			temp2 = HDelete(&minHeap);
			HInsert(&maxHeap, temp2);
			HInsert(&minHeap, temp1);
		}
		printf("%d\n", maxHeap.arr[1]);
	}

	return 0;
}