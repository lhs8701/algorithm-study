#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

int N;
int** S;
int min = INT_MAX;
int* joined;
int flag;

int sumStart() {
	int sum = 0;
	for (int i = 1; i <= N; i++) {
		for (int j = i+1; j <= N; j++) {
			if (joined[i] && joined[j]) 
				sum += (S[i][j] + S[j][i]);
		}
	}
	return sum;
}

int sumLink() {
	int sum = 0;
	for (int i = 1; i <= N; i++) {
		for (int j = i + 1; j <= N; j++) {
			if (!joined[i] && !joined[j])
				sum += (S[i][j] + S[j][i]);
		}
	}
	return sum;
}

void func(int level, int n) {
	if (flag && !joined[1]) {
		printf("%d", min);
		for (int i = 0; i < N + 1; i++)
			free(S[i]);
		free(S);
		free(joined);
		exit(0);
	}
	if (level == N / 2) {
		int result = abs(sumStart() - sumLink());
		if (min > result)
			min = result;
		return;
	}
	if (n == N + 1)
		return;
	flag = 1;
	for (int i = n; i <= N; i++) {
		if (!joined[i]) {
			joined[i] = 1;
			func(level + 1, i + 1);
			joined[i] = 0;
		}
	}
}

int main() {
	scanf("%d%*c", &N);
	S = (int**)malloc(sizeof(int*)*(N+1));
	for (int i = 0; i < N+1; i++)
		S[i] = (int*)malloc(sizeof(int)*(N+1));
	joined = (int*)malloc(sizeof(int)*(N + 1));
	memset(joined, 0, sizeof(int)*(N + 1));

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			scanf("%d", &S[i][j]);
		}
		scanf("%*c");
	}
	func(0,1);

	return 0;
}


