#include <stdio.h>

void print_arr(int *arr, int n) {
	int i = 0;

	while(i < n) {
		printf("%d ", arr[i]);
		i++;
	}

	printf("\n");
}
