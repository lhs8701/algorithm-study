#include<stdio.h>
#include<stdlib.h>
#define MAX 100000

typedef int Data;
typedef struct Stack {
	Data* arr;
	int top;
}Stack;

void StackInit(Stack* pstack) {
	pstack->arr = (Data*)malloc(sizeof(Data) * MAX);
	pstack->top = -1;
}

int SIsEmpty(Stack* pstack) {
	if (pstack->top == -1)
		return 1;
	else
		return 0;
}

void SPush(Stack* pstack, Data data) {
	pstack->arr[++pstack->top] = data;
}

Data SPop(Stack* pstack) {
	return pstack->arr[pstack->top--];
}

Data SPeek(Stack* pstack) {
	return pstack->arr[pstack->top];
}

int main() {
	int n, idx = 0, oIdx = 0, num = 1;
	Stack stack;
	StackInit(&stack);
	scanf("%d%*c", &n);
	int* arr = (int*)malloc(sizeof(int) * n);
	char* oper = (char*)malloc(sizeof(char) * 2 * n);

	for (int i = 0; i < n; i++) {
		scanf("%d%*c", &arr[i]);
	}
	SPush(&stack, num++);
	oper[oIdx++] = '+';
	while (idx < n) {
		if (SPeek(&stack) == arr[idx]) {
			SPop(&stack);
			oper[oIdx++] = '-';
			idx++;
		}
		else {
			if (num > n)
				break;
			SPush(&stack, num++);
			oper[oIdx++] = '+';
		}
	}
	if (!SIsEmpty(&stack))
		printf("NO");
	else {
		for (int i = 0; i < oIdx; i++)
			printf("%c\n", oper[i]);
	}
	return 0;
}