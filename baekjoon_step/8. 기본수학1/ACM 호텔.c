#include <stdio.h>

int main() {
	int T, H, W, N;
	scanf("%d", &T);
	int room, floor;
	for (int i = 0; i < T; i++) {
		scanf("%d %d %d", &H, &W, &N);
		room = N / H + 1;
		floor = N % H;
		if (floor == 0) {
			floor = H;
			room--;
		}
		if (room < 10)
			printf("%d0%d\n", floor, room);
		else
			printf("%d%d\n", floor, room);
	}

	return 0;
}

