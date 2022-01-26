#include<stdio.h>
#include<stdlib.h>
int N, M;

int isPossible(long long tree[], long long length) {
	long long sum = 0;
	for (int i = 0; i < N; i++) {
		if (tree[i] > length) 
			sum += tree[i] - length;
	}
	if (sum >= M) 
		return 1;
	else
		return 0;
}

long long func(long long tree[], long long num) {
	long long left = 1, right = num;
	long long ans = 0;
	while (left <= right) {
		long long mid = (left + right) / 2;
		if (isPossible(tree, mid)) {
			if (ans < mid)
				ans = mid;
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}
	return ans;
}

int main() {
	long long* tree;
	long long max = -1;
	scanf("%d %d%*c", &N, &M);
	tree = (long long*)malloc(sizeof(long long)*N);
	for (int i = 0; i < N; i++) {
		scanf("%lld", &tree[i]);
		if (max < tree[i])
			max = tree[i];
	}
	printf("%lld",func(tree, max));

	return 0;
}