#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N, cnt;
int*row;
int*col;
int*pdiag;
int*mdiag;

void putQueen(int level, int i) {
	row[level] = 1;
	col[i] = 1;
	pdiag[level + i] = 1;
	mdiag[level - i + N - 1] = 1;
}

void delQueen(int level, int i) {
	row[level] = 0;
	col[i] = 0;
	pdiag[level + i] = 0;
	mdiag[level - i + N - 1] = 0;
}

void queenBoard(int level) {
	if (level == N) {
		cnt++;
		return;
	}
	for (int i = 0; i < N; i++) {
		if (!row[level] && !col[i] && !pdiag[level + i] && !mdiag[level - i + N - 1]) {
			putQueen(level, i);
			queenBoard(level + 1);
			delQueen(level, i);
		}
	}
}

int main() {
	scanf("%d", &N);
	
	for (int i = 0; i < N; i++) {
		row = (int*)malloc(sizeof(int)*N);
		col = (int*)malloc(sizeof(int)*N);
	}
	for (int i = 0; i <= 2 * (N - 1); i++) {
		pdiag = (int*)malloc(sizeof(int) * (2 * N - 1));
		mdiag = (int*)malloc(sizeof(int) * (2 * N - 1));
	}
	memset(row, 0, sizeof(int)*N);
	memset(col, 0, sizeof(int)*N);
	memset(pdiag, 0, sizeof(int)*(2 * N - 1));
	memset(mdiag, 0, sizeof(int)*(2 * N - 1));

	queenBoard(0);
	printf("%d", cnt);

	free(row);
	free(col);
	free(pdiag);
	free(mdiag);

	return 0;
}