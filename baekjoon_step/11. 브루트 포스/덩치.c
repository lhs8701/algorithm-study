#include <stdio.h>
#include <stdlib.h>

int main() {
	int N;
	int* grade = NULL;
	int** info = NULL;
	scanf("%d", &N);
	grade = (int*)malloc(sizeof(int)*N);
	info = (int**)malloc(sizeof(int*)*N);
	for (int i = 0; i < N; i++) {
		info[i] = (int*)malloc(sizeof(int) * 2);
		grade[i] = 1;
	}

	for (int i = 0; i < N; i++) 
		scanf("%d %d", &info[i][0], &info[i][1]);

	for (int i = 0; i < N-1; i++) {
		for (int j = i + 1; j < N; j++) {
			if (info[i][0] < info[j][0] && info[i][1] < info[j][1])
				grade[i]++;
			else if (info[i][0] > info[j][0] && info[i][1] > info[j][1])
				grade[j]++;
		}
	}
	
	for (int i = 0; i < N; i++) 
		printf("%d ", grade[i]);
	
	for (int i = 0; i < N; i++)
		free(info[i]);
	free(info);
	free(grade);
	return 0;
}