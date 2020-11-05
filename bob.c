#include <stdio.h>
int main(){
	int test, n,m, step, extra;
	int total;
	int i=0;
	printf ("Enter the number of the testcases : ");
	scanf ("%d",&test);
	for (i=0;i<test;i++){
		printf ("Enter the value of N : ");
		scanf ("%d",&n);
		total = 4*n;
		m= n+1;
		step = total/m;
		extra = total%m;
		if (extra==0){
			printf ("Total no. of moves will be %d\n", step);
		}
		else if (extra>0){
			printf ("Total no. of moves will be %d\n", step+1);
		}
	}
	return 0;
}
