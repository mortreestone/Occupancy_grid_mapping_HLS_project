#include "header.h"
#include "data.h"
#include "grid1.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>



int main()
{
    //f_type grid[XDIM*YDIM];
	f_type grid[16800];


    for(int i=0;i<16800;i++)
        {

    		grid[i]=0;

        }





    for(int i=0;i<1781;i++)
        {

            for(int j=0;j<21;j++)
            {

            	ogm(x_t[i][0],x_t[i][1],x_t[i][2] , angal[j], z_t[i][j],grid);
            }
        }

//        	for(int i=0;i<16800;i++)
//        	{
//        			if(i%XDIM==0)
//        			printf(" %f ,\n",grid[i]);
//        			else
//        			printf(" %f ,",grid[i]);
//
//        	}


//        	printf("\n\n\n\n");

		int ll=L_CONST;
		int iii=I_CONST;

		printf("L=%d, I=%d \n",ll,iii);

    	f_type xx;
    	f_type rate;
    	f_type acc=0;
    	f_type g;
    	for(int i=0;i<(XDIM*YDIM);i++)
    	{

    		xx=abs(test_grid[i]-grid[i]);
    		g=abs(test_grid[i]);
    		rate=((g-xx)/g);
    		if(xx==0&&g==0)
    			{rate=1;}
    		else if(xx!=0&&g==0)
    		{
    			rate=0;
    		}
    		else if(rate<0)
    		{
    			rate=0;
    		}

    		else if (rate>1)
    		{
    			printf("xx= %f grid= %f what's going on\n",xx,test_grid[i]);
    		}



    		grid[i]=rate*100;
    		acc=acc+100-grid[i];

    	}

//    	printf("the accuracy for each cell: \n");
//
//    	for(int i=0;i<16800;i++)
//    	{
//    			if(i%XDIM==0)
//    			printf(" %f ,\n",grid[i]);
//    			else
//    			printf(" %f ,",grid[i]);
//
//    	}

    	acc=100-(acc/16800);
//    	printf("accuracy= %f %%",acc);
    	printf("%f",acc);


    return 0;
}
