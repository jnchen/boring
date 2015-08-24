#include <stdio.h>
int max(int a,int b,int c){
	if(a<b)
		a =b;
	if(a<c)
		a =c;
	return a;
}
typedef int(*FUNC)(int,int,int);

int main(){
	void* p;
	int a,b,c;
	FUNC fun;
	
	p = max;
	
	a = (*((int(*)(int,int,int))p))(1,2,4);
	b = (*(FUNC)p)(1,2,4);
	
	fun = (FUNC)p;
	c = fun(1,2,4);
	printf("%d,%d,%d\n",a,b,c);
}