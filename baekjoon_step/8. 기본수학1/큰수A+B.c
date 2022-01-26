#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void Reverse(char* arr) {
	char temp;
	int len = strlen(arr);
	for (int i = 0; i < len / 2; i++) {
		temp = arr[i];
		arr[i] = arr[len - 1 - i];
		arr[len - 1 - i] = temp;
	}
}

int main() {
	char A[10001];
	char B[10001];
	char C[10002];
	int c = 0, idx = 0, len;
	scanf("%s %s", A, B);
	int pA = strlen(A)-1;
	int pB = strlen(B)-1;
	Reverse(A);
	Reverse(B);

	if (pA < pB) {
		len = pB + 1;
		for (int i = pA + 1; i <= pB; i++) {
			A[i] = '0';
		}
	}
	else {
		len = pA + 1;
		for (int i = pB + 1; i <= pA; i++) {
			B[i] = '0';
		}
	}
	for (int i = 0; i < len; i++) {
		int digit = A[i] - '0' + B[i] - '0' + c;
		C[idx++] = digit % 10 + '0';
		c = digit / 10;
	}
	if (c)
		C[idx++] = '1';
	for (int i = idx - 1; i >= 0; i--) {
		printf("%c", C[i]);
	}

	return 0;
}

