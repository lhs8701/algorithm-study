#include <stdio.h>
#include <math.h>
int countSix(int n) {
	int r = n;
	int cnt = 0;
	while (r != 0) {
		if (r % 10 == 6) 
			cnt++;
		else 
			break;
		r /= 10;
	}
	return cnt;
}

int main() {
	int N, d;
	int n = 0, c, cont, curNumber, order = 1;
	scanf("%d", &N);
	
	while (1) {
		c = n * 1000 + 666;
		cont = countSix(n);
		d = pow(10, cont);
		if (cont == 0) {
			curNumber = c;
		}
		else {
			curNumber = c / d * d;
		}
		if (N < order + d) {
			printf("%d", curNumber + (N - order));
			break;
		}
		n++;
		order += d;
	}

	return 0;
}