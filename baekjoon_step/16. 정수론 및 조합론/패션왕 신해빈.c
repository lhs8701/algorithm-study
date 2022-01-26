#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
	int T, n, flag, result, idx;
	char clothes[21];
	char sort[21];
	char sortArr[30][21];
	int sortCount[30] = { 0, };
	scanf("%d%*c", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d%*c", &n);
		idx = 0;
		for (int j = 0; j < n; j++) {
			scanf("%s%s%*c", clothes, sort);
			flag = 0;
			for (int k = 0; k < idx; k++) {
				if (strcmp(sortArr[k], sort) == 0) {
					flag = 1;
					sortCount[k]++;
					break;
				}
			}
			if (!flag) {
				strcpy(sortArr[idx], sort);
				sortCount[idx] = 1;
				idx++;
			}
		}
		result = 1;
		for (int j = 0; j < idx; j++)
			result *= (sortCount[j] + 1);
		printf("%d\n", result - 1);
	}

	return 0;
}