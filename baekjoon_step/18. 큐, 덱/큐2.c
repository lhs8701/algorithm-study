#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct Queue {
	int*arr;
	int rear;
	int front;
	int size;
}Queue;

void QueueInit(Queue* pq) {
	pq->arr = (int*)malloc(sizeof(int) * 2000000);
	pq->rear = 0;
	pq->front = 0;
	pq->size = 0;
}

int QIsEmpty(Queue* pq) {
	if (pq->front == pq->rear)
		return 1;
	else
		return 0;
}

int getNextIdx(int idx) {
	if (idx == 2000000 - 1)
		return 0;
	else
		return idx + 1;
}

void Enqueue(Queue* pq, int data) {
	pq->rear = getNextIdx(pq->rear);
	pq->arr[pq->rear] = data;
	pq->size++;
}

int Dequeue(Queue*pq) {
	if (QIsEmpty(pq))
		return -1;
	pq->front = getNextIdx(pq->front);
	pq->size--;
	return pq->arr[pq->front];
}

int Size(Queue* pq) {
	return pq->size;
}

int Front(Queue* pq) {
	if (QIsEmpty(pq))
		return -1;
	return pq->arr[getNextIdx(pq->front)];
}

int Back(Queue* pq) {
	if (QIsEmpty(pq))
		return -1;
	return pq->arr[pq->rear];
}

int main() {
	int N;
	char order[10];
	int num;
	Queue que;
	QueueInit(&que);
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", order);
		if (strcmp(order, "push") == 0) {
			scanf("%d%*c", &num);
			Enqueue(&que, num);
		}
		else {
			scanf("%*c");
			if (strcmp(order, "pop") == 0) {
				printf("%d\n", Dequeue(&que));
			}
			else if (strcmp(order, "size") == 0) {
				printf("%d\n", Size(&que));
			}
			else if (strcmp(order, "empty") == 0) {
				printf("%d\n", QIsEmpty(&que));
			}
			else if (strcmp(order, "front") == 0) {
				printf("%d\n", Front(&que));
			}
			else {
				printf("%d\n", Back(&que));
			}
		}
	}

	return 0;
}