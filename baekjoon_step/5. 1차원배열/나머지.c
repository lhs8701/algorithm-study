#include <stdio.h>


int main() {

	int numbers[42] = { 0, };
	int n, cnt = 0;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &n);
		numbers[n % 42]++;
	}
	for (int i = 0; i < 42; i++) {
		if (numbers[i] != 0)
			cnt++;
	}

	printf("%d",cnt);
	return 0;
}

