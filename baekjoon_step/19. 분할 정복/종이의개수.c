#include<stdio.h>
#include<stdlib.h>
int N;
int**arr;
int cnt[3];

int correct(int startX, int startY, int n) {
	int flag = 1;
	char color = arr[startX][startY];
	for (int i = startX; i < startX + n; i++) {
		for (int j = startY; j < startY + n; j++) {
			if (arr[i][j] != color) {
				flag = 0;
				break;
			}
		}
		if (!flag)
			break;
	}
	return flag;
}

void func(int startX, int startY, int n) {
	if (correct(startX, startY, n)) {
		cnt[arr[startX][startY] + 1]++;
		return;
	}
	for (int i = startX; i < startX + n; i += n / 3) {
		for (int j = startY; j < startY + n; j += n / 3) {
			func(i, j, n / 3);
		}
	}
}

int main() {
	scanf("%d%*c", &N);
	arr = (int**)malloc(sizeof(int*)*N);
	for (int i = 0; i < N; i++)
		arr[i] = (int*)malloc(sizeof(int)*N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
		}
		scanf("%*c");
	}

	func(0, 0, N);
	for (int i = 0; i < 3; i++)
		printf("%d\n", cnt[i]);

	for (int i = 0; i < N; i++)
		free(arr[i]);
	free(arr);
	return 0;
}