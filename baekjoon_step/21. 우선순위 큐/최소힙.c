#include<stdio.h>

typedef struct Heap {
	int arr[100001];
	int num;
}Heap;

void HeapInit(Heap* ph) {
	ph->num = 0;
}

int HIsEmpty(Heap* ph) {
	if (ph->num == 0)
		return 1;
	else
		return 0;
}

void HInsert(Heap* ph, int data) {
	int idx = ++ph->num;
	while (idx != 1 && ph->arr[idx / 2] > data) {
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
		return (ph->arr[idx * 2] > ph->arr[idx * 2 + 1]) ? idx * 2 + 1 : idx * 2;
	}
}

int HDelete(Heap* ph) {
	int parent = 1, child;
	int lastElem = ph->arr[ph->num--];
	int RData = ph->arr[1];

	while (child = getPriorChild(ph, parent)) {
		if (lastElem < ph->arr[child])
			break;
		ph->arr[parent] = ph->arr[child];
		parent = child;
	}
	ph->arr[parent] = lastElem;
	return RData;
}

int main() {
	int N, n;
	Heap heap;
	HeapInit(&heap);
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d%*c", &n);
		if (n)
			HInsert(&heap, n);
		else {
			if (HIsEmpty(&heap))
				printf("0\n");
			else
				printf("%d\n", HDelete(&heap));
		}
	}

	return 0;
}