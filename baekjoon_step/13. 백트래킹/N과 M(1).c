#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int N, M;
int* arr;
int* visited;

void func(int level) {
	if (level == M) {
		for (int i = 0; i < M; i++)
			printf("%d ", arr[i]);
		printf("\n");
		return;
	}

	for (int i = 1; i <= N; i++) {
		if (visited[i] == 1)
			continue;
		arr[level] = i;
		visited[i] = 1;
		func(level + 1);
		visited[i] = 0;
	}
}

int main() {
	scanf("%d %d", &N, &M);
	arr = (int*)malloc(sizeof(int)*M);
	visited = (int*)malloc(sizeof(int)*(N + 1));
	memset(visited, 0, sizeof(int)*(N + 1));
	func(0);

	return 0;
}