#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
	
	int arr[4];
	int min,x,y,w,h;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	arr[0] = x; arr[1] = y; arr[2] = w - x; arr[3] = h - y;
	min = arr[0];
	for (int i = 1; i < 4; i++) {
		if (min > arr[i])
			min = arr[i];
	}
	printf("%d", min);

	return 0;
}


