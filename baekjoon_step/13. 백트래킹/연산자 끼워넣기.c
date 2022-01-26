#include <stdio.h>
#include <stdlib.h>
int* arr;
int oper[4];
int min, max;
int N;
struct Stack {
	int arr[10];
	int top;
}typedef Stack;

void StackInit(Stack*pstack) {
	pstack->top = -1;
}
void SPush(Stack*pstack, int data) {
	pstack->arr[++pstack->top] = data;
}
int SPop(Stack*pstack) {
	return pstack->arr[pstack->top--];
}
int SPeek(Stack*pstack) {
	return pstack->arr[pstack->top];
}
int calculation(Stack*pstack) {
	int val = arr[0];
	int oper;
	for (int i = 1; i < N; i++) {
		oper = pstack->arr[i - 1];
		switch (oper) {
		case 0: 
			val += arr[i];
			break;
		case 1:
			val -= arr[i];
			break;
		case 2:
			val *= arr[i];
			break;
		case 3:
			if (val < 0) 
				val = val * -1 / arr[i] * -1;
			else
				val /= arr[i];
			break;
		}
	}
	return val;
}

void func(Stack*pstack,int level) {
	if (level == N - 1) {
		int result = calculation(pstack);
		if (min > result)
			min = result;
		if (max < result)
			max = result;
		return;
	}
	for (int i = 0; i < 4; i++) {
		if (oper[i]) {
			oper[i]--;
			SPush(pstack, i);
			func(pstack, level + 1);
			SPop(pstack);
			oper[i]++;
		}
	}
}

int main() {
	Stack stack;
	StackInit(&stack);
	scanf("%d", &N);
	arr = (int*)malloc(sizeof(int)*N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < 4; i++) {
		scanf("%d", &oper[i]);
	}
	
	min = 1000000001;
	max = -1000000001;
	
	func(&stack, 0);
	printf("%d\n", max);
	printf("%d\n", min);
	free(arr);
	return 0;
}