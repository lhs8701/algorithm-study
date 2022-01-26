#include<stdio.h>
int N;
char arr[64][65];
int correct(int startX, int startY, int endX, int endY) {
	int flag = 1;
	char color = arr[startX][startY];
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
		printf("%d", arr[startX][startY] - '0');
		return;
	}
	printf("(");
	func(startX, startY, midX, midY);
	func(startX, midY + 1, midX, endY);
	func(midX + 1, startY, endX, midY);
	func(midX + 1, midY + 1, endX, endY);
	printf(")");
}

int main() {
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s%*c", arr[i]);
	}
	func(0, 0, N - 1, N - 1);

	return 0;
}