#include<stdio.h>
#include<string.h>
#define MAX 150

typedef char Data;
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
	if (pstack->top == -1) {
		return '0';
	}
	return pstack->arr[pstack->top--];
}
Data SPeek(Stack* pstack) {
	if (pstack->top == -1) {
		return '0';
	}
	return pstack->arr[pstack->top];
}

int main() {
	char str[101];
	int len;
	Stack stack;

	while (1) {
		gets(str);
		if (strcmp(str, ".") == 0)
			break;
		StackInit(&stack);
		len = strlen(str);
		for (int i = 0; i < len; i++) {
			if (str[i] == '(' || str[i] == '[') {
				SPush(&stack, str[i]);
			}
			else if (str[i] == ')') {
				if (SPeek(&stack) == '[' || SPeek(&stack)=='0') {
					SPush(&stack, '0');
					break;
				}
				SPop(&stack);
			}
			else if (str[i] == ']') {
				if (SPeek(&stack) == '(' || SPeek(&stack) == '0') {
					SPush(&stack, '0');
					break;
				}
				SPop(&stack);
			}
		}
		if (SIsEmpty(&stack))
			printf("yes\n");
		else
			printf("no\n");
	}

	return 0;
}