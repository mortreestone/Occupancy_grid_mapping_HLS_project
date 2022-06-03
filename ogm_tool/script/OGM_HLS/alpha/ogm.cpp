#include "header.h"

struct rb
{
	f_type x;
	f_type y;
	f_type theta;
}rbs;


void ogm(f_type xi,f_type yi,f_type thetai, f_type angle, f_type z_t,f_type grid[])
{
#pragma HLS INTERFACE s_axilite port=return
    rbs.x=xi;
    rbs.y=yi;
    rbs.theta=thetai;
    find_cells_to_update_for_ray(angle,z_t,grid);
}

void find_cells_to_update_for_ray( f_type z_theta_t, f_type z_t,f_type grid[])
{

    f_type val = PI / 180;
    f_type inv_cx=(z_theta_t+rbs.theta)*val;
    f_type a_x=A*hls::cos(inv_cx);
    //f_type a_y=A*hls::sin(inv_cx);
    f_type a_y;
    f_type a_x2=a_x*a_x;

    // find a_y without using sin function
    int div=inv_cx/(2*PI);
    f_type rm=inv_cx-(div*PI*2);
    a_y=hls::sqrt((A*A)-a_x2);
    if(((PI<rm))|| ((0>rm)&&(rm>(0-PI))))
	{
    a_y=(0-a_y);
	}


    int x;
    int y;
    int xp,yp;
    f_type length=A;
     f_type index[2]={rbs.x,rbs.y};
     int intex[2];
     get_cell_index3(index,intex);
     x=intex[0];
     y=intex[1];
     grid[(y*XDIM)+x]= grid[(y*XDIM)+x]+hls::log10(PFREE/(1-PFREE))+hls::log10(PRIOR/(1-PRIOR));
     xp=intex[0];
     yp=intex[1];

     f_type r;
     f_type x_f;
     f_type y_f;
     f_type l;

     new_loop: while(length< MAX_RANGE)
     {

         index[0]=index[0]+a_x;
         index[1]=index[1]+a_y;
         get_cell_index3(index,intex);
         x=intex[0];
         y=intex[1];
//         x_f=xcoords[x]+HALF_RESOLUTION-rbs.x;
//         y_f=ycoords[y]+HALF_RESOLUTION-rbs.y;
         x_f=XLIM_F+(x*RESOLUTION)+HALF_RESOLUTION-rbs.x;
         y_f=YLIM_F+(y*RESOLUTION)+HALF_RESOLUTION-rbs.y;
         r= (x_f*x_f)+(y_f*y_f);
         r=hls::sqrt(r);
         l=(r<(z_t-ALFA))?hls::log10(PFREE/(1-PFREE)):0;
         l=(r>(z_t-ALFA))?hls::log10(POCC/(1-POCC)):l;
         l=(r>(z_t+ALFA))?0:l;
         l=(x==xp && y==yp)?0:l;
         grid[(y*XDIM)+x]=grid[(y*XDIM)+x]+l;
         xp=intex[0];
         yp=intex[1];
         length=length+A;
     }


}


void get_cell_index3(f_type *index, int *intex)
{
    int xi;
    int yi;


    xi= ((index[0]-XLIM_F)*IN_RESOLUTION);
    yi= ((index[1]-YLIM_F)*IN_RESOLUTION);


    f_type xc=XLIM_F+(xi*RESOLUTION);
    f_type yc=YLIM_F+(yi*RESOLUTION);
    xi=(index[0]>xc)?xi+1:xi;
    yi=(index[1]>yc)?yi+1:yi;

//    xi=((index[0]>xcoords[xi]))?xi+1:xi;
//    yi=((index[1]>ycoords[yi]))?yi+1:yi;

    xi=(xi<1)?0:xi;
    yi=(yi<1)?0:yi;
    xi=(xi>(XDIM-1))?(XDIM-1):xi;
    yi=(yi>(YDIM-1))?(YDIM-1):yi;

    intex[0]=xi;
    intex[1]=yi;
}
