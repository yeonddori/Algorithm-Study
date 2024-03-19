#include <stdio.h>
#include <string.h>

char original[30005], crypto[30005], key[30005], temp;

int main(){

	gets(original);
	scanf("%s", &key);

	for (int i = 0; i < strlen(original); i++) {
		if (original[i] == ' ')
			crypto[i] = ' ';
		else {
			char temp = original[i] - (key[i % strlen(key)] - 'a') - 1;
			if (temp < 'a')
				temp += 26;
			crypto[i] = temp;
		}
	}

	crypto[strlen(original)] = '\0';
	printf("%s", crypto);
	return 0;
}
