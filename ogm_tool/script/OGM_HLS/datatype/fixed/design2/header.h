#ifndef _HEADER_H_
#define _HEADER_H_

#include "hls_math.h"
#include<stdint.h>
#include<stdio.h>
#include<hls_stream.h>
#include"ap_fixed.h"
#include<stdbool.h>
#include<cmath>


#ifndef POCC
#define POCC 0.8
#endif

#ifndef PFREE
#define PFREE 0.2
#endif

#ifndef PRIOR
#define PRIOR 0.5
#endif

#ifndef ALFA
#define ALFA 0.3
#endif

#ifndef RESOLUTION
#define RESOLUTION 0.5
#endif

#ifndef HALF_RESOLUTION
#define HALF_RESOLUTION 0.25
#endif

#ifndef IN_RESOLUTION
#define IN_RESOLUTION 1/0.5
#endif


//define xlim=[-20,50]
#ifndef XLIM_F
#define XLIM_F -20
#endif

#ifndef XLIM_B
#define XLIM_B 50
#endif

//define xlim=[-30,30]
#ifndef YLIM_F
#define YLIM_F -30
#endif

#ifndef YLIM_B
#define YLIM_B 30
#endif

#ifndef YDIM
#define YDIM 120
#endif

#ifndef XDIM
#define XDIM 140
#endif

#ifndef MAX_RANGE
#define MAX_RANGE 20
#endif

#ifndef A
#define A 0.5
#endif


#ifndef PI
#define PI 3.14159265
#endif

#ifndef VAL
#define VAL 3.14159265/180
#endif

#ifndef L_CONST
#define L_CONST 36
#endif


#ifndef I_CONST
#define I_CONST 7
#endif




//using fix point;
typedef ap_fixed<20,8,AP_RND,AP_WRAP> fix_type;
//typedef ap_fixed<L_CONST,I_CONST> fix_type1;
typedef ap_fixed<L_CONST,I_CONST> fix_type2;
//typedef ap_fixed<32,15> fix_type2;
typedef float fix_type1;
//typedef float fix_type2;
typedef float f_type;
typedef ap_int<16> int_b16;

void ogm(f_type xi,f_type yi,f_type thetai, f_type angle, f_type z_t,f_type grid[]);
//void get_cell_index2(f_type *index);
void get_cell_index3(f_type *index, int_b16 *intex);
void find_cells_to_update_for_ray(f_type z_theta_t, f_type z_t,f_type grid[]);


#endif
