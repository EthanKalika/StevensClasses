/***************************************************************************
 * 
 * Copyright (c) 2024 shudong All Rights Reserved
 * $Id$ 
 * 
 **************************************************************************/
 
 /**
 * @file lab2.c
 * @author Ethan Kalika
 * @date 2024/02/01 22:30:52
 * @version Version 1
 * @brief 
 **/

#include <stdio.h>

struct ST {
    int* p;
};


void swap(struct ST* pa, struct ST* pb) {
    /* Your code here  */
    int* temp = (*pb).p;
    (*pb).p = (*pa).p;
    (*pa).p = temp;
    /* Teacher Example
    int* temp;
    temp = (*pa).p;
    (*pa).p = (*pb).p;
    (*pb).p = temp;

    Note:
    (*pa).p is the same as pa -> p;

    */
}

void strongSwap(struct ST* pa, struct ST* pb)
{
    int** temp = *(pb -> p);
    *(pb -> p) = *(pa -> p);
    *(pb -> p) = temp;
}


int main() {
    
    int a = 10;
    int b = 20;


    struct ST sta = {.p = &a};
    struct ST stb = {.p = &b};


    swap(&sta, &stb);


    printf("*(sta.p) = %d\n*(stb.p) = %d\n", *(sta.p), *(stb.p));
    /* Expected output:  20 10*/

    return 0;
}