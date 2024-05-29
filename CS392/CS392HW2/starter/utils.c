/*******************************************************************************
 * Name        : utils.c
 * Author      : Ethan Kalika
 * Pledge      : I pledge my honor that I have abided by the Stevens Honor System
 ******************************************************************************/
#include "utils.h"

int cmpr_float(void* first, void* second)
{
    if (*((float*)first) > *((float*)second))
    {
        return 1;
    }
    else if (*((float*)first) < *((float*)second))
    {
        return -1;
    }
    return 0;
}

int cmpr_int(void* first, void* second)
{
    if (*((int*)first) > *((int*)second))
    {
        return 1;
    }
    else if (*((int*)first) < *((int*)second))
    {
        return -1;
    }
    
    return 0;
}

void print_int(void* num)
{
    printf("%d ", *((int*)num));
}

void print_float(void* num)
{
    printf("%f ", *((float*)num));
}