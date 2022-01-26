#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct deq {
	int arr[10001];
	int front;
	int rear;
	int size;
}Deq;

int nextPosIdx(int idx) {
	if (idx == 10000)
		return 0;
	else
		return idx + 1;
}

int prePosIdx(int idx) {
	if (idx == 0)
		return 10000;
	else
		return idx - 1;
}
void DeqInit(Deq* pdeq) {
	pdeq->front = 0;
	pdeq->rear = 0;
	pdeq->size = 0;
}
void push_front(Deq*pdeq, int data) {
	pdeq->arr[pdeq->front] = data;
	pdeq->front = prePosIdx(pdeq->front);
	pdeq->size++;
}
void push_back(Deq*pdeq, int data) {
	pdeq->rear = nextPosIdx(pdeq->rear);
	pdeq->arr[pdeq->rear] = data;
	pdeq->size++;
}
int empty(Deq*pdeq) {
	if (pdeq->front == pdeq->rear)
		return 1;
	else
		return 0;
}
int pop_front(Deq*pdeq) {
	if (empty(pdeq))
		return -1;
	pdeq->front = nextPosIdx(pdeq->front);
	pdeq->size--;
	return pdeq->arr[pdeq->front];
}
int pop_back(Deq*pdeq) {
	int rData = pdeq->arr[pdeq->rear];
	if (empty(pdeq))
		return -1;
	pdeq->rear = prePosIdx(pdeq->rear);
	pdeq->size--;
	return rData;
}
int size(Deq*pdeq) {
	return pdeq->size;
}

int front(Deq*pdeq) {
	if (empty(pdeq))
		return -1;
	return pdeq->arr[nextPosIdx(pdeq->front)];
}
int back(Deq*pdeq) {
	if (empty(pdeq))
		return -1;
	return pdeq->arr[pdeq->rear];
}
int main() {
	Deq deq;
	DeqInit(&deq);
	int N, num;
	char order[20];
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", order);
		if (strcmp(order, "push_back") == 0 || strcmp(order, "push_front") == 0) {
			scanf("%d%*c", &num);
			if (strlen(order) > 9) {
				push_front(&deq, num);
			}
			else {
				push_back(&deq, num);
			}
		}
		else if (strcmp(order, "pop_front") == 0) {
			printf("%d\n",pop_front(&deq));
		}
		else if (strcmp(order, "pop_back") == 0) {
			printf("%d\n", pop_back(&deq));
		}
		else if (strcmp(order, "size") == 0) {
			printf("%d\n", size(&deq));
		}
		else if (strcmp(order, "empty") == 0) {
			printf("%d\n", empty(&deq));
		}
		else if (strcmp(order, "front") == 0) {
			printf("%d\n", front(&deq));
		}
		else {
			printf("%d\n", back(&deq));
		}
	}
	return 0;
}