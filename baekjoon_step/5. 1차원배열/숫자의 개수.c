#include <stdio.h>


int main() {
	int n, num = 1;
	int r, digit;
	int numbers[10] = {0,};

	for (int i = 0; i < 3; i++) {
		scanf("%d", &n);
		num *= n;
	}

	r = num;
	while (r != 0) {
		digit = r % 10;
		numbers[digit]++;
		r /= 10;
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n", numbers[i]);
	}

	return 0;
}

