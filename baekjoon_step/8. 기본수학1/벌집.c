#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int N;
	scanf("%d", &N);
	int x = 1, cnt = 1;
	while (N > x) {
		x += 6 * cnt;
		cnt++;
	}
	printf("%d", cnt);

	return 0;
}

