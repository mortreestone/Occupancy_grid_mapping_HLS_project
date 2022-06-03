#include "header.h"
#include "data.h"
#include "grid_1.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

float acc(float grid[],int result[]);

float acc(float grid[],int result[])
{
    float a=0;
    for(int i=0;i<(YDIM*XDIM);i++)
    {
        if(grid[i]==result[i])
        {
            a=a+1;
            //printf("%d,%f \n",result[i],grid[i]);
            //printf("%d\n",a);
        }
        

    }
    float accuracy=a/(YDIM*XDIM)*100;
    //printf("%f\n",accuracy);
    return accuracy;
}


int main()
{
    //d_type grid[XDIM*YDIM];
	float grid[YDIM*XDIM];


    for(int i=0;i<YDIM*XDIM;i++)
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



    for(int i=0;i<YDIM*XDIM;i++)
    {
        if(grid[i]>0)
            grid[i]=1;
        else
            grid[i]=0;        
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

		// int ll=L_CONST;
		// int iii=I_CONST;

		// printf("L=%d, I=%d \n",ll,iii);

    	// d_type xx;
    	// d_type rate;
    	// d_type acc=0;
    	// d_type g;
    	// for(int i=0;i<(XDIM*YDIM);i++)
    	// {

    	// 	xx=abs(test_grid[i]-grid[i]);
    	// 	g=abs(test_grid[i]);
    	// 	rate=((g-xx)/g);
    	// 	if(xx==0&&g==0)
    	// 		{rate=1;}
    	// 	else if(xx!=0&&g==0)
    	// 	{
    	// 		rate=0;
    	// 	}
    	// 	else if(rate<0)
    	// 	{
    	// 		rate=0;
    	// 	}

    	// 	else if (rate>1)
    	// 	{
    	// 		printf("xx= %f grid= %f what's going on\n",xx,test_grid[i]);
    	// 	}



    	// 	grid[i]=rate*100;
    	// 	acc=acc+100-grid[i];

    	// }

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

    	float accu;
        int lenthogm= (YDIM*XDIM);
        switch(lenthogm)
        {
            case 268800:
                accu=acc(grid,grid125);
                break;
            case 67200:
                accu=acc(grid,grid25);
                break;
            case 16800:
                accu=acc(grid,grid5);
                break;
            case 4200:
                accu=acc(grid,grid1);
                break;         
            case 1050:
                accu=acc(grid,grid1);
                break;                                         

        }

        


    	printf("%f",accu);
    	
        //printf("%f",accu);


    return 0;
}