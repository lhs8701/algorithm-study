#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int T, max;
	int a[3];
	while (1) {
		scanf("%d %d %d", &a[0], &a[1], &a[2]);
		if (!a[0] && !a[1] && !a[2])
			break;
		max = a[0];
		for (int i = 1; i < 3; i++) {
			if (max < a[i])
				max = a[i];
		}
		if (a[0] * a[0] + a[1] * a[1] + a[2] * a[2] - max*max == max*max)
			printf("right\n");
		else
			printf("wrong\n");
	}

	return 0;
}


