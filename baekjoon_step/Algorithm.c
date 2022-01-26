/*


< 에라토스테네스의 체 (1~N 사이의 소수 구하기) >

void Eratosthenes(int* num, int N){
	num[1] = 1;
	for (int i = 2; i*i <= N; i++) {
		if (num[i])
			continue;
		for (int j = i*i; j <= N; j += i) {
			num[j] = 1;
		}
	}
}
 ※num[x] == 0 이면 소수, 1이면 합성수

< 백트래킹(기본) >

void func(int level, int M) {
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
		visited[i] = 1;   * 핵심 
		func(level + 1);  * 핵심
		visited[i] = 0;   * 핵심
	}
}

< LCS (최장 공통 부분 수열) >

void LCS (char* str1, char* str2) {
	for (int i = 0; i < n1; i++) {
		for (int j = 0; j < n2; j++) {
			if (str1[i] == str2[j])
				dp[i+1][j+1] = dp[i][j] + 1;
			else
				dp[i+1][j+1] = Max(dp[i+1][j], dp[i][j+1]);
		}
	}
}

< 유클리드 호제법 >

int gcd(int n1, int n2) {
	int temp;
	while (n2 != 0) {
		temp = n1%n2;
		n1 = n2;
		n2 = temp;
	}
	return n1;
}

int lcm(int n1, int n2) {
	return n1*n2 / gcd(n1, n2);
}

<Binary Search>
int binarySearch(int*arr, int N, int key) {
	int left = 0, right = N - 1, mid;
	while (left <= right) {
		mid = (left + right) / 2;
		if (arr[mid] == key)
			return mid;
		else if (arr[mid] > key)
			right = mid - 1;
		else
			left = mid + 1;
	}
	return -1;
}
<Upper Bound & Lower Bound>
* right = 배열 크기 N으로 설정해야 함 ! 

int lowerBound(int* arr, int N, int key) {
	int left = 0, right = N, mid;
	while (left < right) {
		mid = (left + right) / 2;
		if (arr[mid] >= key)
			right = mid;
		else
			left = mid + 1;
	}
	return right;
}

int upperBound(int* arr, int N, int key) {
	int left = 0, right = N, mid;
	while (left < right) {
		mid = (left + right) / 2;
		if (arr[mid] > key)
			right = mid;
		else
			left = mid + 1;
	}
	return right;
}

<KMP 알고리즘>

void getFailure(int*fail, char*W) {
	* fail배열 0으로 초기화 *
	int M = strlen(W);
	for (int i = 1, j = 0; i < M; i++) {
		while (j > 0 && W[i] != W[j])
			j = fail[j - 1];
		if (W[i] == W[j])
			fail[i] = ++j;
	}
}

int kmp(int* failure, char* string, char* pat) {
	int N = strlen(string);
	int M = strlen(pat);
	for (int i = 0, j = 0; i < N; i++) {
		while (j > 0 && string[i] != pat[j])
			j = failure[j - 1];
		if (string[i] == pat[j]) {
			if (j == M - 1)
				return i - M + 1;
			else
				j++;
		}
	}
	return -1;
}

*/