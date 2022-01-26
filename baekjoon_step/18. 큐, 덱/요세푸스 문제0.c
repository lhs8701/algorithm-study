#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef int Data;
typedef struct Queue {
	Data*arr;
	int rear;
	int front;
	int valid;
}Queue;
int N;

void QueueInit(Queue* pq) {
	pq->arr = (Data*)malloc(sizeof(Data) * N);
	pq->rear = 0;
	pq->front = 0;
	pq->valid = 0;
}

int getNextIdx(int idx) {
	if (idx == N - 1)
		return 0;
	else
		return idx + 1;
}

void Enqueue(Queue* pq, Data data) {
	pq->rear = getNextIdx(pq->rear);
	pq->arr[pq->rear] = data;
	pq->valid++;
}

void func(Queue*pq, int K, int* result) {
	int cur = pq->front;
	int cnt, idx = 0;
	while (pq->valid != 1) {
		cnt = 0;
		while (cnt < K) {
			cur = getNextIdx(cur);
			if (pq->arr[cur] != 0)
				cnt++;
		}
		result[idx++] = pq->arr[cur];
		pq->arr[cur] = 0;
		pq->valid--;
	}
	while (pq->arr[cur] == 0)
		cur = getNextIdx(cur);
	result[idx] = pq->arr[cur];
}

int main() {
	int K;
	int result[1000];
	Queue que;
	QueueInit(&que);
	scanf("%d %d%*c", &N, &K);
	for (int i = 1; i <= N; i++) {
		Enqueue(&que, i);
	}
	func(&que, K, result);
	printf("<");
	for (int i = 0; i < N-1; i++)
		printf("%d, ",result[i]);
	printf("%d>", result[N - 1]);

	return 0;
}