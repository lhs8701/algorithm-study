#include <stdio.h>

int getDownNum(int num) {
	if (num == 0)
		return 23;
	else
		return --num;
}

int main() {
	int H, M;
	scanf("%d", &H);
	scanf("%d", &M);

	if (M < 45)
		printf("%d %d", getDownNum(H), 15 + M);
	else
		printf("%d %d", H, M - 45);

	return 0;
}

