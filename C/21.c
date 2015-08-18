#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void ShowState(int iNumber[],int bState[], int n, int nKey){
	int i,flag=1;
	for (i = 1; i<n; i++){
		if (bState[i] == 1)
			if (flag){
				printf("%d", iNumber[i]);
				flag = 0;
			}
			else
				printf("+%d", iNumber[i]);
	}
	printf("=%d\n", nKey);
}
void Func(int iNumber[],int nPos, int bAdd, int nSum, int bState[], int len, int nKey){
	if (bAdd == 1){
		nSum += iNumber[nPos];
		bState[nPos] = 1;
	}
	else
		bState[nPos] = 0;
	if (nSum == nKey){
		ShowState(iNumber,bState, len, nKey);
		return;
	}
	if (nPos + 1 == len)return;
	Func(iNumber,nPos + 1, 1, nSum, bState, len, nKey);
	Func(iNumber,nPos + 1, 0, nSum, bState, len, nKey);
}
int checkSum(int iNumber[],int len,int nKey){
	int i,sum=0;
	for(i=1;i<len;i++){
		sum+=iNumber[i];
	}
	if(sum>nKey)
		return 1;
	else 
		return 0;
}

int main(){
	int *iNumber,*tNumber, i, nKey,len;
	printf("Please input the len of Array:");
	scanf("%d",&len);
	if(len>0){
		len++;
		iNumber = (int *)malloc(sizeof(int)*len);
		tNumber = (int *)malloc(sizeof(int)*len);
		memset(tNumber,0,sizeof(int)*len);
		
		iNumber[0] = 0;
		printf("Please input the Number of Array:");
		for(i=1;i<len;i++){
			scanf("%d",iNumber+i);
		}
		printf("Please input the Sum:");
		scanf("%d",&nKey);
		if(checkSum(iNumber,len,nKey)){
			Func(iNumber,0,0,0,tNumber,len,nKey);
		}else{
			printf("The Sum too Big!!\n");
		}
	}
	return 0;
}
