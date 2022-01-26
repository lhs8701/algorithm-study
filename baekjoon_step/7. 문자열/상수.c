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
	char num1[4];
	char num2[4];
	scanf("%s %s", num1, num2);
	getReverse(num1);
	getReverse(num2);
	
	if (atoi(num1) > atoi(num2))
		printf("%s", num1);
	else
		printf("%s", num2);


}

