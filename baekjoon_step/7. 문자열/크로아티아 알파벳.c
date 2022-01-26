#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char input[101];
	int cnt = 0;

	scanf("%s", input);
	int len = strlen(input);
	for (int i = len-1; i >= 0; i--) {
		char tok = input[i];
		if (tok == '=') {
			if (input[i - 1] == 'c' || input[i - 1] == 's')
				cnt++;
			else if (input[i - 1] == 'z') {
				cnt++;
				if (i - 2 >= 0 && input[i - 2] == 'd')
					cnt++;
			}
		}
		else if (tok == '-') {
			cnt++;
		}
		else if (tok == 'j') {
			if (i-1 >=0 && (input[i-1] == 'l' || input[i-1] == 'n')){
				cnt++;
			}
		}
	}
	printf("%d", len - cnt);
	return 0;
}

