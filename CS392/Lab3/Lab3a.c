/***************************************************************************
 * 
 * Copyright (c) 2024 shudong All Rights Reserved
 * $Id$ 
 * 
 **************************************************************************/
 
 /**
 * @file lab0209a.c
 * @author shudong(shudong)
 * @date 2024/02/09 15:32:02
 * @version $Revision$ 
 * @brief 
 **/

#include <stdio.h>

struct ArrayList {
    void* array;
    void (*init_arr)(struct ArrayList*,int,int);
    void (*destroy)(struct ArrayList*);
};

// My attempt
/*
void init_arr (struct ArrayList* arrlist, int length, int type)
{
    if (type == 1)
    {
        return malloc(length * 4); // replace hard coding these numbers with size of
    }
    else
    {
        return malloc(length * 8);  // do not return, instead set the pointer in the struct
    }
}
*/

void initialize(struct ArrayList* parr, int len, int type){
    if (type == 1) parr->array = malloc(len * sizeof(int));
    else parr->array = malloc(len * sizeof(float));
}

int main() {
    struct ArrayList p;
    p.init_arr = initialize;
    p.init_arr(&p, 10, 1);
    return 0;
}