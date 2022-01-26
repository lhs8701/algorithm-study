#include <stdio.h>


int main() {
	int num, max=-1, idx;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &num);
		if (max < num) {
			max = num;
			idx = i;
		}
	}
	printf("%d\n%d", max, idx+1);

	return 0;
}

