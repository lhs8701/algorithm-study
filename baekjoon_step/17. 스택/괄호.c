#include<stdio.h>
#include<string.h>
#define MAX 51

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
		return 0;
	return pstack->arr[pstack->top--];
}
Data SPeek(Stack* pstack) {
	if (pstack->top == -1)
		return -1;
	return pstack->arr[pstack->top];
}

int main() {
	int T, len;
	char str[51];
	Stack stack;
	scanf("%d%*c", &T);
	for (int i = 0; i < T; i++) {
		StackInit(&stack);
		scanf("%s", str);
		len = strlen(str);
		for (int j = 0; j < len; j++) {
			if (str[j] == '(') 
				SPush(&stack, 1);
			else {
				if (SPop(&stack) == 0) {
					SPush(&stack, 1);
					break;
				}
			}
		}
		if (SIsEmpty(&stack))
			printf("YES\n");
		else
			printf("NO\n");
	}
	

	return 0;
}