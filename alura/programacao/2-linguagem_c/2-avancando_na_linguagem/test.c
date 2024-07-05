# include <stdio.h>

int main() {

    char guesses[26];

    for (int i = 0; i < 26; i++) {

        guesses[i] = 65 + i;
        printf("%c ", guesses[i]);
    }
    
}
