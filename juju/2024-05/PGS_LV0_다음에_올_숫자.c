#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// common_len은 배열 common의 길이입니다.
int solution(int common[], size_t common_len) {
    int answer = 0;
    if((common[0]+common[2])==(2*common[1])){
        answer =  (2*common[(common_len-1)]-common[(common_len-2)]);
    }
    else if((common[0]*common[2])==(common[1]*common[1])){
        answer =(common[(common_len-1)] * common[(common_len-1)]/common[(common_len-2)]);
    }
    return answer;
}