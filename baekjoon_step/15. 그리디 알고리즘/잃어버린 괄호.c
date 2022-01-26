#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#define MAX 6

typedef struct Queue {
	int front;
	int rear;
	int arr[MAX];
}Queue;

void QueueInit(Queue* que) {
	que->front = 0;
	que->rear = 0;
}

int QIsEmpty(Queue* que) {
	if (que->front == que->rear)
		return 1;
	else
		return 0;
}

int getNextIdx(int idx) {
	if (idx + 1 == MAX)
		return 0;
	else
		return idx + 1;
}

void Enqueue(Queue* que, char data) {
	if (getNextIdx(que->rear) == que->front)
		return;
	que->rear = getNextIdx(que->rear);
	que->arr[que->rear] = data;
}

char Dequeue(Queue* que) {
	if (QIsEmpty(que))
		return 'X';
	que->front = getNextIdx(que->front);
	return que->arr[que->front];
}


int main() {
	Queue que;
	char str[52];
	int len, num=0, sum = 0, mflag = 0, digit = -1;
	QueueInit(&que);
	scanf("%s", str);
	len = strlen(str);
	for (int i = 0; i < len; i++) {
		if (isdigit(str[i])) {
			Enqueue(&que, str[i]);
			digit++;
		}
		else {
			while (!QIsEmpty(&que))
				num += (Dequeue(&que) - '0')*pow(10, digit--);
			if (str[i] == '-') {
				if (mflag) {
					sum -= num;
				}
				else {
					sum += num;
					mflag = 1;
				}
				num = 0;
			}
		}
	}
	while (!QIsEmpty(&que))
		num += (Dequeue(&que) - '0')*pow(10, digit--);
	if (mflag)
		sum -= num;
	else
		sum += num;
	printf("%d", sum);
	return 0;
}