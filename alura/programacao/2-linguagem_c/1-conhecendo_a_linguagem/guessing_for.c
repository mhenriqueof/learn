# include <stdio.h>

# define TRIES 5

int main() {

    // shows the game header
    printf("--------------------------------\n");
    printf("| Welcome to the Guessing Game |\n");
    
    int pc_number = 42;

    int us_number;

    for (int i = 1; i <= TRIES; i++) {

        printf("--------------------------------\n");

        printf("Try %d of %d\n", i, TRIES);
        printf("What is your guess? \n");
        scanf("%d", &us_number);

        if (us_number < 0) {

            printf("You can type negative numbers!\n");
            i--;
            continue;

        }
    
        int correct = (us_number == pc_number);
        int higher = (us_number > pc_number);

        printf("[%d] ", us_number);

        if (correct) {

            printf("Congratulations! You got it!\n");
            break;

        } else if (higher) {

            printf("your guess is high!\n");
            
        } else {
                
            printf("your guess is low!\n");

        }
    }
    printf("Game over!");
}    
