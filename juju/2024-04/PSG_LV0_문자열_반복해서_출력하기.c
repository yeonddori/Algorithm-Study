#include <stdio.h>
#define LEN_INPUT 11

int main(void) {
    char s1[LEN_INPUT];
    int a;
    scanf("%s %d", s1, &a);
    int i = 0;
    while(i<a){
        printf(s1);
        i++;
    }
    return 0;
}