
#include <stdio.h>
#include <math.h>

int hello(int j);

int hello(int j){
    int i;
    int sum = 0;
    for(i=0; i<j; ++i){
        sum += cos(0.1);
        // printf("hello world: %d\n", sum);
    }
    
    return sum;
}