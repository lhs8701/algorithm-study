#include<stdio.h>
int N;
int arr[128][128];
int cnt[2];
int correct(int startX, int startY, int endX, int endY) {
	int flag = 1;
	int color = arr[startX][startY];
	for (int i = startX; i <= endX; i++) {
		for (int j = startY; j <= endY; j++) {
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

void func(int startX, int startY, int endX, int endY) {
	int midX = (startX + endX) / 2, midY = (startY + endY) / 2;
	if (correct(startX, startY, endX, endY)) {
		cnt[arr[startX][startY]]++;
		return;
	}
	func(startX, startY, midX, midY);
	func(midX + 1, startY, endX, midY);
	func(startX, midY + 1, midX, endY);
	func(midX + 1, midY + 1, endX, endY);
}

int main() {
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &arr[i][j]);
		}
		scanf("%*c");
	}
	func(0, 0, N - 1, N - 1);
	printf("%d\n", cnt[0]);
	printf("%d\n", cnt[1]);
	return 0;
}