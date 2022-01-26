#include <stdio.h>
#include <stdlib.h>

int main() {

	int T;
	char string[80];
	int sum, cnt;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		sum = 0;
		cnt = 0;
		scanf("%s", string);
		for (int j = 0; j < strlen(string); j++) {
			char tok = string[j];
			if (tok == 'O') {
				cnt++;
				sum += cnt;
			}
			else {
				cnt = 0;
			}
		}
		printf("%d\n", sum);
	}

	return 0;
}

