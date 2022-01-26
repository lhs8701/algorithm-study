#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int N;

typedef struct _queue {
	int* arr;
	int rear;
	int front;
}Queue;

void QueueInit(Queue*pq) {
	pq->rear = -1;
	pq->front = 0;
	pq->arr = (int*)malloc(sizeof(int)*N);
}
int nextPosIdx(int idx) {
	if (idx == N-1)
		return 0;
	else
		return idx + 1;
}
int prePosIdx(int idx) {
	if (idx == 0)
		return N-1;
	else
		return idx - 1;
}
void Enqueue(Queue*pq, int data) {
	pq->rear = nextPosIdx(pq->rear);
	pq->arr[pq->rear] = data;
}
int Dequeue(Queue*pq) {
	int RData = pq->arr[pq->front];
	pq->front = nextPosIdx(pq->front);
	return RData;
}
void REnqueue(Queue*pq, int data) {
	pq->front = prePosIdx(pq->front);
	pq->arr[pq->front] = data;
}
int RDequeue(Queue*pq) {
	int rData = pq->arr[pq->rear];
	pq->rear = prePosIdx(pq->rear);
	return rData;
}
int Front(Queue*pq) {
	return pq->arr[nextPosIdx(pq->front)];
}
int func1(Queue*pq) {
	return Dequeue(pq);
}
void func2(Queue*pq) {
	Enqueue(pq, Dequeue(pq));
}
void func3(Queue* pq) {
	REnqueue(pq, RDequeue(pq));
}

int rightCycle(Queue*pq, int idx) {
	if (idx == pq->rear)
		return pq->front;
	else
		return nextPosIdx(idx);
}
int leftCycle(Queue*pq, int idx) {
	if (idx == pq->front)
		return pq->rear;
	else
		return prePosIdx(idx);
}
int rightDir(Queue* pq, int n) {
	int cur = pq->front;
	int d = 0;
	while (pq->arr[cur] != n) {
		cur = rightCycle(pq,cur);
		d++;
	}
	return d;
}
int leftDir(Queue* pq, int n) {
	int cur = pq->front;
	int d = 0;
	while (pq->arr[cur] != n) {
		cur = leftCycle(pq, cur);
		d++;
	}
	return d;
}

int main() {
	int N, M, num, rd, ld, cnt=0;
	int arr[50];
	Queue que;
	QueueInit(&que);
	scanf("%d %d%*c", &N, &M);
	for (int i = 0; i < M; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 1; i <= N; i++) {
		Enqueue(&que, i);
	}
	for (int i = 0; i < M; i++) {
		num = arr[i];
		rd = rightDir(&que, num);
		ld = leftDir(&que, num);
		if (rd <= ld) {
			for (int j = 0; j < rd; j++)
				func2(&que);
			func1(&que);
			cnt += rd;	
		}
		else {
			for (int j = 0; j < ld; j++)
				func3(&que);
			func1(&que);
			cnt += ld;
		}
	}
	printf("%d\n",cnt);
	
	return 0;
}