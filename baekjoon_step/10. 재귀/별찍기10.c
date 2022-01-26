#include <stdio.h>
#include <stdlib.h>

void f2(int N, char** arr, int x, int y) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			arr[y+i][x+j] = ' ';
		}
	}
}

void f1(int N, char** arr, int x, int y) {
	if (N == 1) {
		arr[y][x] = '*';
		return;
	}
	f1(N / 3, arr, y, x);
	f1(N / 3, arr, y, x+N/3);
	f1(N / 3, arr, y, x+2*N/3);
	f1(N / 3, arr, y+N/3, x);
	f2(N / 3, arr, y+N/3, x+N/3);
	f1(N / 3, arr, y+N/3, x+2*N/3);
	f1(N / 3, arr, y+2*N/3, x);
	f1(N / 3, arr, y+2*N/3, x+N/3);
	f1(N / 3, arr, y+2*N/3, x+2*N/3);
}

int main() {
	int N;
	char** arr = NULL;
	arr = (char**)malloc(sizeof(char*) * 3000);
	for (int i = 0; i < 3000; i++) 
		arr[i] = (char*)malloc(sizeof(char) * 3000);
	
	scanf("%d", &N);
	f1(N, arr, 0, 0);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%c", arr[i][j]);
		}
		printf("\n");
	}
	for (int i = 0; i < 3000; i++)
		free(arr[i]);
	free(arr);
	return 0;
}


