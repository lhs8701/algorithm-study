#include <stdio.h>
#include <stdlib.h>

int board[9][9];
int row[9][10];
int col[9][10];
int square[9][10];

void completeBoard(int level) {
	int x = level / 9, y = level % 9;
	if (level == 81) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++)
				printf("%d ", board[i][j]);
			printf("\n");
		}
		exit(0);
	}
	if (board[x][y] != 0) {
		completeBoard(level + 1);
		return;
	}
	for (int i = 1; i < 10; i++) {
		if (!row[x][i] && !col[y][i] && !square[3 * (x / 3) + y / 3][i]) {
			board[x][y] = i;
			row[x][i] = 1;
			col[y][i] = 1;
			square[3 * (x / 3) + y / 3][i] = 1;
			completeBoard(level + 1);
			board[x][y] = 0;
			row[x][i] = 0;
			col[y][i] = 0;
			square[3 * (x / 3) + y / 3][i] = 0;
		}
	}
}

int main() {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &board[i][j]);
			row[i][board[i][j]] = 1;
			col[j][board[i][j]] = 1;
			square[3 * (i / 3) + j / 3][board[i][j]] = 1;
		}
		scanf("%*c");
	}

	completeBoard(0);

	return 0;
}