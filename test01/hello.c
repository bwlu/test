#include <stdio.h>
int main()
{
	int num;
    printf("����һ�����֣�");
    scanf("%d",&num);
    printf("num=%d\n",num);
    int i=0;
    while(i<num){
    	printf("i=%d ",i);
    	i++;
	}
	for(i=0;i<num;i++){
		printf("i=%d ",i);
	}
    return 0;
}
