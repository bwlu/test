#include <stdio.h>
int main()
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
	for(i=0;i<n;i++){
    	for(j=0;j<n;j++){
			arr3[i][j] = 0;
			for(k=0;k<n;k++){
				arr3[i][j] += arr1[i][k] * arr2[k][j];
			}
		}
	}
	printf("������˽��: \n");
	for(i=0;i<n;i++){
    	for(j=0;j<n;j++){
    		printf("%d",arr3[i][j]);
    		printf(" ");
		}
		printf("\n");
	}
	return 0;
}

