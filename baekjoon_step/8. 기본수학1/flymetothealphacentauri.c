#include <stdio.h>
#include <math.h>
int main() {
	int T, x, y,dis;
	int p, cnt;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d %d", &x, &y);
		cnt = 0;
		dis = y - x;
		p = 2;
		while (1) {
			if (dis < pow(p, 2)) {
				int n = dis - pow((p - 1),2);
				int j = p - 1;
				while (n != 0) {
					cnt += n / j;
					n %= j;
					j--;
				}
				break;
			}
			p++;
		}
		printf("%d\n", cnt + 2*(p - 1) - 1);
	}

	return 0;
}

