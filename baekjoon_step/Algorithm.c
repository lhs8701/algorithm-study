/*


< �����佺�׳׽��� ü (1~N ������ �Ҽ� ���ϱ�) >

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
 ��num[x] == 0 �̸� �Ҽ�, 1�̸� �ռ���

< ��Ʈ��ŷ(�⺻) >

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
		visited[i] = 1;   * �ٽ� 
		func(level + 1);  * �ٽ�
		visited[i] = 0;   * �ٽ�
	}
}

< LCS (���� ���� �κ� ����) >

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

< ��Ŭ���� ȣ���� >

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
* right = �迭 ũ�� N���� �����ؾ� �� ! 

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

<KMP �˰���>

void getFailure(int*fail, char*W) {
	* fail�迭 0���� �ʱ�ȭ *
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