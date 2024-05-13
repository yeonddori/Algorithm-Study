#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len) {
    int i = 0;
    while(i < array_len){
        if(array[i]>=array[i+1]){
            int x = array[i];
            array[i] = array[i+1];
            array[i+1] = x;
        }
        i++;
    }
    int a = (array_len) / 2;
    return array[a];
}