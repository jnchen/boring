#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ARRAY_SIZE 84   //此处修改数组大小 

double iNumber[ARRAY_SIZE+1] = {
	0,58643.5,38161.5,60610,178172.5,51062.5,40185,33288,8607,48488,1710,15779.5,47348,16644,8322,48488,241395,59222.5,115415.5,42427,15675,60876,42085,54549,17242.5,38807.5,29469,23579,30305,28215,6935,78793,4104,7837.5,45543,20805,23579,61275,12910.5,4303.5,52240.5,26353,12483,69445,4303.5,4303.5,32680,24111,15257,8322,2869,5738,12122,15675,42892.5,45543,37449,27740,14345,8607,23512.5,24244,6840,60876,34675,16644,17214,18648.5,15675,18183,13680,40850,29469,31901,27740,8607,8607,4702.5,24244,6840,92653.5,95313.5,24244,22230,3135
};//首位没用，初始化是也要写 

void ShowState(FILE* fp,int bState[], int n, double nKey){
	int i,flag=1;
	for (i = 1; i<n; i++){
		if (bState[i] == 1)
			if (flag){
				printf("%g", iNumber[i]);
				fprintf(fp,"%g",iNumber[i]);
				flag = 0;
			}
			else{
				printf("+%g", iNumber[i]);
				fprintf(fp,"+%g",iNumber[i]);
			}
				
	}
	printf("=%g\n", nKey);
	fprintf(fp,"=%g\n",nKey);
}
void Func(FILE* fp,int nPos, int bAdd, double nSum, int bState[], int len, double nKey){
	if (bAdd == 1){
		nSum += iNumber[nPos];
		bState[nPos] = 1;
	}
	else
		bState[nPos] = 0;
	if(nSum>nKey)return;
	else if (nSum == nKey){
		ShowState(fp,bState, len, nKey);
		return;
	}
	if (nPos + 1 == len)return;
	Func(fp,nPos + 1, 1, nSum, bState, len, nKey);
	Func(fp,nPos + 1, 0, nSum, bState, len, nKey);
}

int main(){
	int *tNumber, i;
	double nKey,sum=0.0;
	char * filename="output.txt";
	FILE *fp;
	for (i = 0; i < ARRAY_SIZE	+1; ++i){
		sum += iNumber[i];
	}
	tNumber = (int*)malloc(sizeof(int)*(ARRAY_SIZE+1));
	memset(tNumber, 0, sizeof(int)*(ARRAY_SIZE+1));
	printf("Please input the Sum:");
	scanf("%lf", &nKey);
	if (sum < nKey) {printf("The Sum is too Big!!");
		return 0;
	}
	fp = fopen(filename,"w");
	if(fp==NULL)return 0;	
	Func(fp,0, 0, 0, tNumber, ARRAY_SIZE+1, nKey);
	fclose(fp);
	return 0;
}
