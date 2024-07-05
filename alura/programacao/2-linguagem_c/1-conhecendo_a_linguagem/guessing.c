# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <time.h>

int main() {

    // shows the game header
    // printf("--------------------------------\n");
    // printf("| Welcome to the Guessing Game |\n");
    // printf("--------------------------------\n\n");

    printf("\n");
    printf("          P  /_\\  P                             \n");
    printf("         /_\\_|_|_/_\\                           \n");
    printf("     n_n | ||. .|| | n_n         Welcome to the  \n");
    printf("     |_|_|nnnn nnnn|_|_|         Guessing Game!  \n");
    printf("    |" "  |  |_|  |"  " |                        \n");
    printf("    |_____| ' _ ' |_____|                        \n");
    printf("          \\__|_|__/                             \n\n");
    
    srand(time(NULL));

    int pc_number = rand() % 100;
    int us_number;
    int tries = 1;
    float score = 1000;

    // Ask game difficulty
    int tries_number;
    int level;
    printf("Which difficulty do you want to play?\n[1] Easy [2] Medium [3] Hard ");
    scanf("%d", &level);

    switch (level) {

        case 1:
            tries_number = 20;
            break;

        case 2:
            tries_number = 10;
            break;
        
        default:
            tries_number = 5;
    }

    int correct;

    printf("pc number: %d\n", pc_number);

    for (int i = 1; i <= tries_number; i++) {

        printf("Try %d of %d\n", i, tries_number);

        // Ask user guess
        printf("What is your guess? \n");
        scanf("%d", &us_number);

        // Verify if number isn't grater than 0
        if (us_number < 0) {

            printf("You can't type negative numbers!\n");
            continue;

        }
    
        correct = (us_number == pc_number);
        int higher = (us_number > pc_number);

        // Conditions comparing guess and the real number
        if (correct) {
            printf("You got it!\n");
            break;

        } else if (higher) {
            printf("your guess is high!\n");
            
        } else {               
            printf("your guess is low!\n");

        }

        tries++;

        // Calculating the user score
        float ponto = abs(us_number - pc_number) / 2.0;
        score = score - ponto;

        printf("--------------------------------\n");
    }

    printf("Game over! ");

    if (correct) {
        printf("You won!\nYour tries was: %d and your score was: %.2f", tries, score);
    } else {
        printf("You lose!\n");
    }

}    
