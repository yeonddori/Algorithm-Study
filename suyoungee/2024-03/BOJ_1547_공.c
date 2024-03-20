#include <stdio.h>

void exchange(int num1, int num2);
int cup[3] = {1, 2, 3};
int main(){
    int M = 0;
    int a = 0, b = 0;

    scanf("%d", &M);

    for (int i = 0; i < M; i++) {
        scanf("%d %d", &a, &b);

        exchange(a, b);
    }
    printf("%d", cup[0]);
}

void exchange(int num1, int num2){
    int x = 0, y = 0;
    for(int i = 0; i < 3; i++){
        if(cup[i] == num1)
            x = i;
    }
    for(int i = 0; i < 3; i++){
        if(cup[i] == num2)
            y = i;
    }
    int temp = cup[x];
    cup[x] = cup[y];
    cup[y] = temp;
}
