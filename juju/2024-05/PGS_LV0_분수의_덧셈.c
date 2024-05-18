#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int numer1, int denom1, int numer2, int denom2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*2);
    int numer3 = (numer1 * denom2) + (numer2 * denom1);
    int denom3 = denom1 * denom2;
    int i = numer3;
    while(i > 0){
        if((numer3%i)==0 & (denom3%i)==0){
            numer3=numer3/i;
            denom3=denom3/i;
        }
        i--;
    }
    answer[0] = numer3;
    answer[1] = denom3;
    return answer;
}