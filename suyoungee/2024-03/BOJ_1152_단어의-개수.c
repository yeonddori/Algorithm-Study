// 2024-03-14

#include <stdio.h>
#include <string.h>

int main() {

    char arr[1000000];
    int i,cnt=0; // count for spaces

    // %[^\n] : receiving input as a string until a new line is encountered, including whitespace
    scanf("%[^\n]", arr);

    int len = strlen(arr);

    if (len == 1) { // when only a single space is entered
        if (arr[i] == ' ') { // In C language, single quotation marks('') should be used when comparing characters in strings.
            printf("0\n");
            return 0;
        }
    }

    for (i=1; i<len-1; i++) { // exclude leading and trailing spaces
        if (arr[i] == ' ') cnt++;
    }

    printf("%d", cnt+1);

    return 0;
}
