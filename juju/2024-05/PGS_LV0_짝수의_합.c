#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int sum = 0;
    int i = 1;
    while(i <= n){
        if(i%2==0){
            sum = sum + i;
        }
        i++;
    }
    return sum;
}