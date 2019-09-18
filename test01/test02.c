#include <stdio.h>

void multiply(int *A, int *B, int *C, int n){
	int i,j,k;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			C[i*n+j] = 0;
			for(k=0;k<n;k++){
				C[i*n+j] += A[i*n+k] * B[k*n+j];
			}
		}
	}
}
int main2()
{
	int n;
	printf("������������: ");
	scanf("%d",&n);
    int arr1[n][n];
    int arr2[n][n];
    int arr3[n][n];
    int i,j,k;
    printf("�������һ������: \n");
    for(i=0;i<n;i++){
    	for(j=0;j<n;j++){
    		scanf("%d",&arr1[i][j]);
		}
	}
	printf("������ڶ�������: \n");
	for(i=0;i<n;i++){
    	for(j=0;j<n;j++){
    		scanf("%d",&arr2[i][j]);
		}
	}
    multiply(arr1, arr2, arr3, n);
    printf("������˽��: \n");
    for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			printf("%d", arr3[i][j]);
			printf(" ");
		}
		printf("\n");
	}
	return 0;
}

