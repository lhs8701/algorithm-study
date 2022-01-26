#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct Stack {
	int arr[100000];
	int top;
}Stack;

void StackInit(Stack* pstack) {
	pstack->top = -1;
}

int SIsEmpty(Stack* pstack) {
	if (pstack->top == -1)
		return 1;
	else
		return 0;
}

void SPush(Stack* pstack, int data) {
	pstack->arr[++pstack->top] = data;
}

int SPop(Stack* pstack) {
	return pstack->arr[pstack->top--];
}

int gcd(int a, int b) {
	int temp;
	while (b != 0) {
		temp = a%b;
		a = b;
		b = temp;
	}
	return a;
}

int main() {
	int N, num,g,n, idx=0;
	int arr[100];
	int result[100000];
	Stack stack;
	StackInit(&stack);
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++)
		scanf("%d%*c", &arr[i]);
	g = abs(arr[1] - arr[0]);
	for (int i = 2; i < N; i++) {
		num = abs(arr[i] - arr[i - 1]);
		g = gcd(num, g);
	}
	for (int i = 2; i < g; i++) {
		if (g%i == 0) {
			n = g / i;
			if (i < n) {
				result[idx++] = i;
				SPush(&stack, n);
			}
			else {
				if (i == n)
					result[idx++] = i;
				break;
			}
		}
	}
	while (!SIsEmpty(&stack))
		result[idx++] = SPop(&stack);
	result[idx++] = g;
	for (int i = 0; i < idx; i++)
		printf("%d ", result[i]);

	return 0;
}