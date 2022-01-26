#include <stdio.h>

void func(int num, int* arr) {
	int r = num;
	int i = 0;

	while (r != 0) {
		arr[i++] = r % 10;
		r /= 10;
	}
	return;
}

int main() {
	int arr[3];
	int A, B;
	scanf("%d", &A);
	scanf("%d", &B);

	func(B, arr);
	printf("%d\n", arr[0] * A);
	printf("%d\n", arr[1] * A);
	printf("%d\n", arr[2] * A);
	printf("%d\n", A*B);

	return 0;
}

