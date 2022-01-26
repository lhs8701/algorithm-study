#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Queue {
	int front;
	int rear;
	int arr[6];
}Queue;

int main() {
	Queue que;
	char str[52];
	int len, num, sum = 0, mflag = 0;
	QueueInit(&que);
	scanf("%s", str);
	len = strlen(str);
	for (int i = 0; i < len; i++) {
		if (isdigit(str[i]))
			Enqueue(&que, str[i]);
		else {
			while (!QIsEmpty)
				num += Dequeue(&que) - '0';
			if (str[i] == '-') {
				if (mflag) {
					sum -= num;
					num = 0;
				}
				else {
					sum += num;
					num = 0;
					mflag = 1;
				}
			}
		}
	}
	while (!QIsEmpty)
		num += Dequeue(&que) - '0';
	if (mflag)
		sum -= num;
	else
		sum += num;
	printf("%d", sum);
	return 0;
}