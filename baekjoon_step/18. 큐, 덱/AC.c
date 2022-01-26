#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
typedef int Data;
typedef struct Queue {
	Data* arr;
	int front;
	int rear;
}Queue;

void QueueInit(Queue* pq) {
	pq->arr = (Data*)malloc(sizeof(Data) * 100005);
	pq->front = 0;
	pq->rear = 0;
}

int QIsEmpty(Queue* pq) {
	if (pq->rear == pq->front)
		return 1;
	else
		return 0;
}

void Enqueue(Queue* pq, Data data) {
	pq->arr[++pq->rear] = data;
}

Data Dequeue(Queue*pq) {
	return pq->arr[++pq->front];
}

Data RDequeue(Queue*pq) {
	return pq->arr[pq->rear--];
}

void Print(Queue* pq, int state) {
	printf("[");
	if (state > 0) {
		for (int i = pq->front + 1; i < pq->rear; i++) {
			printf("%d,", pq->arr[i]);
		}
		printf("%d]\n", pq->arr[pq->rear]);
	}
	else {
		for (int i = pq->rear; i > pq->front + 1; i--) {
			printf("%d,", pq->arr[i]);
		}
		printf("%d]\n", pq->arr[pq->front + 1]);
	}
}

int main() {
	int T, num, flag, lenFunc, lenArr, state;
	char* func = (char*)malloc(sizeof(char) * 100000);
	char* arr = (char*)malloc(sizeof(char) * 10000030);

	Queue que;
	scanf("%d%*c", &T);
	for (int t = 0; t < T; t++) {
		QueueInit(&que);
		scanf("%s%*c", func);
		scanf("%d%*c", &num);
		scanf("%s%*c", arr);
		flag = 1;
		state = 1;
		lenFunc = strlen(func);
		lenArr = strlen(arr);
		
		char* ptr = strtok(arr, "[,]");
		while (ptr != NULL) {
			Enqueue(&que, atoi(ptr));
			ptr = strtok(NULL, "[,]");
		}
		for (int i = 0; i < lenFunc; i++) {
			if (func[i] == 'R') {
				state *= -1;
			}
			else {
				if (QIsEmpty(&que)) {
					flag = 0;
					break;
				}
				if (state == 1) 
					Dequeue(&que);
				else 
					RDequeue(&que);
			}
		}
		if (QIsEmpty(&que)) {
			if (flag)
				printf("[]\n");
			else
				printf("error\n");
		}
		else
			Print(&que, state);
	}
	free(arr);
	free(func);

	return 0;
}