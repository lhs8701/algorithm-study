#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getReverse(char* num) {
	char temp;
	temp = num[2];
	num[2] = num[0];
	num[0] = temp;
}

int main() {
	char input[16];
	int alpha[26] = { 2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9 };
	scanf("%s", input);
	int len = strlen(input);
	int sum = 0;
	for (int i = 0; i < len; i++) {
		char tok = input[i];
		sum += alpha[tok - 'A'];
	}

	printf("%d", sum + len);

}

