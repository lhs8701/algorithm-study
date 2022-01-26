#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 500001

typedef int Data;
typedef struct Queue {
	Data*arr;
	int rear;
	int front;
}Queue;

void QueueInit(Queue* pq) {
	pq->arr = (Data*)malloc(sizeof(Data) * MAX);
	pq->rear = 0;
	pq->front = 0;
}

int QIsEmpty(Queue* pq) {
	if (pq->front == pq->rear)
		return 1;
	else
		return 0;
}

int getNextIdx(int idx) {
	if (idx == MAX - 1)
		return 0;
	else
		return idx + 1;
}

void Enqueue(Queue* pq, Data data) {
	if (getNextIdx(pq->rear) == pq->front) {
		printf("Queue Full\n");
		exit(0);
	}
	pq->rear = getNextIdx(pq->rear);
	pq->arr[pq->rear] = data;
}

Data Dequeue(Queue*pq) {
	if (QIsEmpty(pq)) {
		printf("Queue Empty\n");
		exit(0);
	}
	pq->front = getNextIdx(pq->front);
	return pq->arr[pq->front];
}

void func(Queue* pq) {
	while (getNextIdx(pq->front) != pq->rear) {
		Dequeue(pq);
		Enqueue(pq, Dequeue(pq));
	}
}

int main() {
	int N;
	Queue que;
	QueueInit(&que);
	scanf("%d%*c", &N);
	for (int i = 1; i <= N; i++)
		Enqueue(&que, i);
	func(&que);
	printf("%d", Dequeue(&que));

	return 0;
}