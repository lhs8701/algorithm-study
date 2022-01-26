#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char input[1000000];
	int alpha[26] = { 0, };
	int max = -1, maxAlpha = -1, flag=0;
	scanf("%s", input);
	int len = strlen(input);
	for (int i = 0; i < len; i++) {
		if (input[i] - 'a' < 0) {
			alpha[input[i] - 'A' ]++;
		}
		else {
			alpha[input[i] - 'a']++;
		}
	}
	for (int i = 0; i < 26; i++) {
		if (max < alpha[i]) {
			max = alpha[i];
			maxAlpha = i;
			flag = 0;
		}
		else if (max == alpha[i]) {
			flag = 1;
		}
	}

	if (flag == 1)
		printf("?");
	else
		printf("%c", 'A' + maxAlpha);

	return 0;
}

