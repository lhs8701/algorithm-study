#include<stdio.h>
#include<stdlib.h>
#define MAX 1000000

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

void freeStack(Stack* pstack) {
	free(pstack->arr);
}

int main() {
	int N;
	Stack stack;

	scanf("%d%*c", &N);
	int* arr = (int*)malloc(sizeof(int)*N);
	int* result = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++) 
		scanf("%d", &arr[i]);
		
	StackInit(&stack);
	
	for (int i = N - 1; i >= 0; i--) {
		while (!SIsEmpty(&stack) && SPeek(&stack) <= arr[i]) {
			SPop(&stack);
		}
		if (SIsEmpty(&stack))
			result[i] = -1;
		else
			result[i] = SPeek(&stack);
		SPush(&stack,arr[i]);
	}

	for (int i = 0; i < N; i++)
		printf("%d ", result[i]);
	free(arr);
	free(result);
	
	return 0;
}
