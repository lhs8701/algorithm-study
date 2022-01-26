#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct _box {
	int order;
	int data;
}Box;

typedef struct _queue {
	Box arr[101];
	int front;
	int rear;
}Queue;
void QueueInit(Queue* pq) {
	memset(pq->arr, 0, sizeof(pq->arr));
	pq->front = 0;
	pq->rear = 0;
}

int QIsEmpty(Queue* pq) {
	if (pq->rear == pq->front)
		return 1;
	else
		return 0;
}

int nextPosIdx(int idx) {
	if (idx == 100)
		return 0;
	else
		return idx + 1;
}

void Enqueue(Queue* pq, Box data) {
	pq->rear = nextPosIdx(pq->rear);
	pq->arr[pq->rear] = data;
}

Box Dequeue(Queue* pq) {
	pq->front = nextPosIdx(pq->front);
	return pq->arr[pq->front];
}

int main() {
	int T, N, M;
	int priority[10] = { 0, };
	int flag, order, n;
	Queue que;
	Box box, num;
	scanf("%d%*c", &T);
	for (int t = 0; t < T; t++) {
		QueueInit(&que);
		memset(priority, 0, sizeof(priority));
		scanf("%d %d%*c", &N, &M);
		for (int i = 0; i < N; i++) {
			scanf("%d", &n);
			box.order = i;
			box.data = n;
			priority[n]++;
			Enqueue(&que, box);
		}
		scanf("%*c");
		order = 1;
		while (!QIsEmpty(&que)) {
			num = Dequeue(&que);
			flag = 1;
			for (int i = num.data + 1; i < 10; i++) {
				if (priority[i] != 0) {
					flag = 0;
					break;
				}
			}
			if (flag) {
				if (num.order == M) {
					printf("%d\n", order);
					break;
				}
				else {
					order++;
					priority[num.data]--;
				}
			}
			else {
				Enqueue(&que, num);
			}
		}
	}
	return 0;
}