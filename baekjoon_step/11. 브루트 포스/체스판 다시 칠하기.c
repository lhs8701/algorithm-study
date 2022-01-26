#include <stdio.h>
#include <stdlib.h>

char chessW[8][8];
char chessB[8][8];

int test(char**board, int y, int x) {
	int cntW = 0, cntB = 0;
	for (int i = y; i < y+8; i++) {
		for (int j = x; j < x+8; j++) {
			if (board[i][j] != chessW[i-y][j-x])
				cntW++;
			if (board[i][j] != chessB[i-y][j-x])
				cntB++;
		}
	}
	return (cntW < cntB) ? cntW : cntB;
}

int main() {
	int N, M;
	char** board = NULL;
	int num, min;

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (i % 2 == 0 && j % 2 == 0 || i % 2 == 1 && j % 2 == 1) {
				chessW[i][j] = 'W';
				chessB[i][j] = 'B';
			}
			else {
				chessW[i][j] = 'B';
				chessB[i][j] = 'W';
			}
		}
	}

	scanf("%d %d%*c", &N, &M);

	board = (char**)malloc(sizeof(char*)*N);
	for (int i = 0; i < N; i++)
		board[i] = (char*)malloc(sizeof(char)*(M+1));

	for (int i = 0; i < N; i++) {
		gets(board[i]);
	}

	min = M*N;
	for (int i = 0; i <= N - 8; i++) {
		for (int j = 0; j <= M - 8; j++) {
			num = test(board, i, j);
			if (min > num) 
				min = num;
		}
	}
	printf("%d", min);

	for (int i = 0; i < N; i++)
		free(board[i]);
	free(board);

	return 0;
}