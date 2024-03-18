#include <stdio.h>

int main() {

    int n;
    scanf("%d", &n);

    int giveup = 1;
    char name[40];
    int count[27] = {0};

    for (int i=0; i<n; i++) {
        scanf("%s", name);
        count[name[0]-'a']++;
    }

    for (int i=0; i<26; i++) {
        if (count[i] >= 5) {
            printf("%c", i+'a');
            giveup = 0;
        }
    }

    if (giveup == 1) printf("PREDAJA");

    return 0;
}
