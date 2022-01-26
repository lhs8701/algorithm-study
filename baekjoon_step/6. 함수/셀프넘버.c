#include <stdio.h>
#include <stdlib.h>

int d(int num) {
	int r = num;
	int sum = r;
	while (r != 0) {
		sum += (r % 10);
		r /= 10;
	}
	if (sum > 10000)
		return -1;
	return sum;
}

int main() {
	int numbers[10001] = { 0, };
	for (int i = 1; i <= 10000; i++) {
		int n = d(i);
		if (n == -1)
			continue;
		numbers[n]++;
	}
	for (int i = 1; i <= 10000; i++) {
		if (numbers[i] == 0)
			printf("%d\n", i);
	}

}

