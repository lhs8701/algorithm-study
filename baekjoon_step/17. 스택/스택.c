#include<stdio.h>
#include<string.h>
#define MAX 10000

typedef int Data;
typedef struct Stack {
	int top;
	Data arr[MAX];
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
void SPush(Stack* pstack, Data data) {
	if (pstack->top == MAX - 1) {
		printf("Stack Full\n");
		return;
	}
	pstack->arr[++pstack->top] = data;
}
Data SPop(Stack* pstack) {
	if (pstack->top == -1)
		return -1;
	return pstack->arr[pstack->top--];
}
Data SPeek(Stack* pstack) {
	if (pstack->top == -1)
		return -1;
	return pstack->arr[pstack->top];
}

int main() {
	int N;
	Data data;
	char str[10];
	Stack stack;
	StackInit(&stack);
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", str);
		if (strcmp(str, "push") == 0) {
			scanf("%d%*c", &data);
			SPush(&stack, data);
		}
		else if (strcmp(str, "pop") == 0) {
			printf("%d\n", SPop(&stack));
		}
		else if (strcmp(str, "size") == 0) {
			printf("%d\n", stack.top+1);
		}
		else if (strcmp(str, "empty") == 0) {
			printf("%d\n", SIsEmpty(&stack));
		}
		else {
			printf("%d\n", SPeek(&stack));
		}
	}
	return 0;
}