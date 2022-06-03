#include "header.h"

//const int ll=L_CONST;
//const int iii=I_CONST;

//typedef ap_fixed<ll,iii> fix_type1;
//typedef ap_fixed<ll,iii> fix_type2;

struct rb
{
	f_type x;
	f_type y;
	f_type theta;
}rbs;

fix_type2 const xcoords[XDIM]={ -20.00000,-19.500000, -19.000000, -18.500000, -18.000000, -17.500000, -17.000000, -16.500000, -16.000000,
		-15.500000, -15.000000, -14.500000, -14.000000, -13.500000, -13.000000, -12.500000, -12.000000, -11.500000, -11.000000,
		-10.500000, -10.000000, -9.500000, -9.000000, -8.500000, -8.000000, -7.500000, -7.000000, -6.500000, -6.000000, -5.500000,
		-5.000000, -4.500000, -4.000000, -3.500000, -3.000000, -2.500000, -2.000000, -1.500000, -1.000000, -0.500000, 0.000000, 0.500000,
		1.000000, 1.500000, 2.000000, 2.500000, 3.000000, 3.500000, 4.000000, 4.500000, 5.000000, 5.500000, 6.000000, 6.500000,
		7.000000, 7.500000, 8.000000, 8.500000, 9.000000, 9.500000, 10.000000, 10.500000, 11.000000, 11.500000,
		12.000000, 12.500000, 13.000000, 13.500000, 14.000000, 14.500000, 15.000000, 15.500000, 16.000000, 16.500000,
		17.000000,17.500000, 18.000000, 18.500000, 19.000000, 19.500000, 20.000000, 20.500000, 21.000000, 21.500000, 22.000000,
		22.500000, 23.000000, 23.500000, 24.000000, 24.500000, 25.000000, 25.500000, 26.000000, 26.500000, 27.000000, 27.500000,
		28.000000, 28.500000, 29.000000, 29.500000, 30.000000, 30.500000, 31.000000, 31.500000, 32.000000, 32.500000, 33.000000,
		33.500000, 34.000000, 34.500000, 35.000000, 35.500000, 36.000000, 36.500000, 37.000000, 37.500000, 38.000000,
		38.500000,39.000000, 39.500000, 40.000000, 40.500000, 41.000000, 41.500000, 42.000000, 42.500000, 43.000000, 43.500000,
		44.000000, 44.500000, 45.000000, 45.500000, 46.000000, 46.500000, 47.000000, 47.500000, 48.000000, 48.500000, 49.000000, 49.500000};

fix_type2 const ycoords[YDIM]={-30.000000,-29.500000, -29.000000, -28.500000, -28.000000, -27.500000, -27.000000, -26.500000, -26.000000, -25.500000,
		-25.000000, -24.500000, -24.000000, -23.500000, -23.000000, -22.500000, -22.000000, -21.500000, -21.000000, -20.500000, -20.000000,
		-19.500000, -19.000000, -18.500000, -18.000000, -17.500000, -17.000000, -16.500000, -16.000000, -15.500000, -15.000000, -14.500000,
		-14.000000, -13.500000, -13.000000, -12.500000, -12.000000, -11.500000, -11.000000, -10.500000, -10.000000, -9.500000, -9.000000,
		-8.500000, -8.000000, -7.500000, -7.000000, -6.500000, -6.000000, -5.500000, -5.000000, -4.500000, -4.000000, -3.500000, -3.000000,
		-2.500000, -2.000000, -1.500000, -1.000000, -0.500000, 0.000000, 0.500000, 1.000000, 1.500000, 2.000000, 2.500000, 3.000000, 3.500000,
		4.000000, 4.500000, 5.000000, 5.500000, 6.000000, 6.500000, 7.000000, 7.500000, 8.000000, 8.500000, 9.000000, 9.500000, 10.000000,
		10.500000, 11.000000, 11.500000, 12.000000, 12.500000, 13.000000, 13.500000, 14.000000, 14.500000, 15.000000, 15.500000, 16.000000,
		16.500000, 17.000000, 17.500000, 18.000000, 18.500000, 19.000000, 19.500000, 20.000000, 20.500000, 21.000000, 21.500000, 22.000000,
		22.500000, 23.000000, 23.500000, 24.000000, 24.500000, 25.000000, 25.500000, 26.000000, 26.500000, 27.000000, 27.500000, 28.000000,
		28.500000, 29.000000, 29.500000};

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

	fix_type1 val = PI / 180;
	fix_type1 theta_fixed=z_theta_t+rbs.theta;
	fix_type1 inv_cx_f=(theta_fixed)*val;
	fix_type1 fa=A;
	fix_type1 a_x_f=(fix_type1)A*hls::cos((fix_type1)(inv_cx_f));
	fix_type1 inv_cx=inv_cx_f;
	fix_type1 a_x=a_x_f;
	fix_type1 a_y;
	fix_type1 a_x2=a_x*a_x;

    // find a_y without using sin function
	fix_type1 twopi=2*PI;
    int div=inv_cx/twopi;
    fix_type1 rm=inv_cx-(div*twopi);
    a_y=hls::sqrt((fa*fa)-a_x2);
    if(((PI<rm))|| ((0>rm)&&(rm>(0-PI))))
	{
    a_y=(0-a_y);
	}


    int_b16 x;
    int_b16 y;
    int_b16 xp,yp;
    fix_type2 length=A;
     f_type index[2]={rbs.x,rbs.y};
     int_b16 intex[2];
     get_cell_index3(index,intex);
     x=intex[0];
     y=intex[1];
     grid[(y*XDIM)+x]= (fix_type2)grid[(y*XDIM)+x]+hls::log10((fix_type2)(PFREE/(1-PFREE)))+hls::log10((fix_type2)(PRIOR/(1-PRIOR)));
     xp=intex[0];
     yp=intex[1];

     fix_type2 r;
     fix_type2 r_fix;
     fix_type2 x_f;
     fix_type2 y_f;
     fix_type2 rfx=rbs.x;
	 fix_type2 rfy=rbs.y;
	 fix_type2 f_h=HALF_RESOLUTION;
	 fix_type2 l;
     f_type fa_x=a_x;
     f_type fa_y=a_y;



     new_loop: while(length< MAX_RANGE)
     {
         index[0]=index[0]+fa_x;
         index[1]=index[1]+fa_y;
         get_cell_index3(index,intex);
         x=intex[0];
         y=intex[1];
         x_f=xcoords[x]+f_h-rfx;
         y_f=ycoords[y]+f_h-rfy;
         x_f=x_f*x_f;
         y_f=y_f*y_f;
         r_fix= x_f+y_f;
         r_fix=hls::sqrt(r_fix);
         r=r_fix;
         l=(r<(fix_type2)(z_t-ALFA))?(fix_type2)hls::log10((fix_type2)(PFREE/(1-PFREE))):(fix_type2)0;
         l=(r>(fix_type2)(z_t-ALFA))?(fix_type2)hls::log10((fix_type2)(POCC/(1-POCC))):l;
         l=(r>(fix_type2)(z_t+ALFA))?(fix_type2)0:l;
         l=(x==xp && y==yp)?(fix_type2)0:l;
         grid[(y*XDIM)+x]=(fix_type2)grid[(y*XDIM)+x]+l;
         xp=intex[0];
         yp=intex[1];
         length=length+(fix_type2)A;
     }
}


void get_cell_index3(f_type *index, int_b16 *intex)
{
	int_b16 xi;
	int_b16 yi;
	int_b16 zero=0;
	int_b16 xmax=XDIM-1;
	int_b16 ymax=YDIM-1;
    fix_type f1=index[0];
    fix_type f2=index[1];
    fix_type fr=RESOLUTION;
    xi= ((f1-XLIM_F)/fr)+1;
    yi= ((f2-YLIM_F)/fr)+1;
    xi=((f1>(fix_type)xcoords[xi]))?(fix_type)(xi+1):(fix_type)xi;
    yi=((f2>(fix_type)ycoords[yi]))?(fix_type)(yi+1):(fix_type)yi;
    xi=(xi<1)?zero:xi;
    yi=(yi<1)?zero:yi;
    xi=(xi>(XDIM-1))?xmax:xi;
    yi=(yi>(YDIM-1))?ymax:yi;
    intex[0]=xi;
    intex[1]=yi;
}



