#include <stdio.h>
#include <math.h>
void hanoi(int x, int dep, int des) {
	int des2;
	if (x == 1) {
		printf("%d %d\n", dep, des);
		return;
	}
	des2 = 6 - (dep + des);
	hanoi(x - 1, dep, des2);
	printf("%d %d\n",dep, des);
	hanoi(x - 1, des2, des);
}

int main() {
	int N, cnt = 0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) 
		cnt += pow(2, i - 1);
	
	printf("%d\n", cnt);
	hanoi(N, 1, 3);

	return 0;
}