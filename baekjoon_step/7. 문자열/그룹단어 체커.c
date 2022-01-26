#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int N;
	char str[101];
	int alpha[26];
	int i, j, flag=1, cnt=0;

	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%s", str);
		flag = 1;
		j = 0;
		memset(alpha, 0, sizeof(alpha));
		int len = strlen(str);
		while (j < len) {
			char tok = str[j];
			int num = str[j] - 'a';
			if (alpha[num] == 0) {
				alpha[num]++;
				while (str[j] == tok) {
					j++;
				}
			}
			else {
				flag = 0;
				break;
			}
		}
		if (flag)
			cnt++;
	}
	printf("%d", cnt);

	return 0;
}

