#include <stdio.h>

int func(int N) {
	int num = N;
	int a, b,cnt=0;
	while (1) {
		a = num % 10;
		if (num / 10 == 0)
			b = 0;
		else
			b = num / 10;
		num = a * 10 + (a + b)%10;
		cnt++;
		if (num == N)
			break;
	}
	return cnt;
}

int main() {
	int N;
	scanf("%d", &N);
	printf("%d", func(N));

	return 0;
}

