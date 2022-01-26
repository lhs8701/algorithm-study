#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int N, num, max = -1;
	int* arr;
	int numbers[10001] = { 0, };
	int b[10001] = { 0, };
	
	scanf("%d%*c", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d%*c", &num);
		numbers[num]++;
		if (max < num)
			max = num;
	}
	for (int i = 1; i <= max; i++)
		b[i] = b[i - 1] + numbers[i];

	for (int i = 1; i <= max; i++) {
		for (int j = b[i - 1]; j < b[i]; j++)
			printf("%d\n", i);
	}
	return 0;
}