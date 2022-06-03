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


#ifndef PALFA
#define PALFA 0.3
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

#ifndef PRESOLUTION
#define PRESOLUTION 1
#endif

#ifndef PYDIM
#define PYDIM 60
#endif

#ifndef PXDIM
#define PXDIM 70
#endif

#ifndef PA
#define PA 1
#endif



#ifndef RESOLUTION
#define RESOLUTION (float)PRESOLUTION
#endif

#ifndef HALF_RESOLUTION
#define HALF_RESOLUTION RESOLUTION/2
#endif

#ifndef IN_RESOLUTION
#define IN_RESOLUTION 1/RESOLUTION
#endif


#ifndef YDIM
#define YDIM (int)PYDIM
#endif

#ifndef XDIM
#define XDIM (int)PXDIM
#endif

#ifndef A
#define A (float)PA
#endif

#ifndef ALFA
#define ALFA (float)PALFA
#endif


#ifndef MAX_RANGE
#define MAX_RANGE 20
#endif


#ifndef PI
#define PI 3.14159265
#endif

#ifndef VAL
#define VAL 3.14159265/180
#endif


//using fix point;
//typedef ap_fixed<12,20,AP_RND,AP_WRAP> f_type;
typedef float f_type;

void ogm(f_type xi,f_type yi,f_type thetai, f_type angle, f_type z_t,f_type grid[]);
//void get_cell_index2(f_type *index);
void get_cell_index3(f_type *index, int *intex);
void find_cells_to_update_for_ray(f_type z_theta_t, f_type z_t,f_type grid[]);


#endif
