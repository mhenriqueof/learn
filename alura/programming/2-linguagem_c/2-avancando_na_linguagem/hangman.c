# include <stdio.h>
# include <string.h>
# include <ctype.h>
# include <stdlib.h>
# include <time.h>
# include "hangman.h"


int chutes_dados = 0;
char chutes[26];
char palavra_secreta[TAMANHO_PALAVRA];

void opening() {
	printf("|-----------------|\n");
	printf("|- Jogo de Forca -|\n");
	printf("|-----------------|\n");
}

int chutes_errados() {

	int erros = 0;
	for (int i = 0; i < chutes_dados; i++) {
		int existe = 0;
		for (int j = 0; j <= (int)strlen(palavra_secreta); j++) {
			if (chutes[i] == palavra_secreta[j]) {
				existe = 1;
				break;
			}
		}
		if (!existe) erros++;
	}

	return erros;

}

int enforcou() {

	return chutes_errados() >= 5;
}

void chuta() {
	char chute;
	printf("Letra: ");
	scanf(" %c", &chute);
	chute = toupper(chute);

	chutes[chutes_dados] = chute;
	(chutes_dados)++;
}

int ja_chutou(char letra) {
	int achou = 0;
	for (int j = 0; j < chutes_dados; j++) {
		if (toupper(chutes[j]) == toupper(letra)) {
			achou = 1;
			break;
		}
	}

	return achou;
}

int acertou() {
	for (int i = 0; i < (int)strlen(palavra_secreta); i++) {
		if (!ja_chutou(palavra_secreta[i])) {
			return 0;
		}
	}
	return 1;
}

void desenha_forca() {

	int erros = chutes_errados();

    printf("  _______       \n");
	printf(" |/      |      \n");
	printf(" |      %c%c%c  \n", (erros >= 1 ? '(' : ' '), (erros >= 1 ? '_' : ' '), (erros >= 1 ? ')' : ' '));
	printf(" |      %c%c%c  \n", (erros >= 2 ? '\\' : ' '), (erros >= 2 ? '|' : ' '), (erros >= 2 ? '/' : ' '));
	printf(" |       %c     \n", (erros >= 3 ? '|' : ' '));
	printf(" |      %c %c   \n", (erros >= 4 ? '/' : ' '), (erros >= 4 ? '\\' : ' '));
	printf(" |              \n");
	printf("_|___           \n");

	printf("\n\n");

    int tamanho = strlen(palavra_secreta);
    for (int i = 0; i < tamanho; i++) {

        int achou = ja_chutou(palavra_secreta[i]);

        if (achou) {
            printf("%c ", palavra_secreta[i]);
        } else {
            printf("_ ");
        }
    }
    printf("\n");
}

void adiciona_palavra() {

	int opcao;
	printf("Adicionar palavra? [1] SIM | [0] NAO ");
	scanf("%d", &opcao);

	if (opcao == 1) {
		char nova_palavra[TAMANHO_PALAVRA];
		printf("Palavra: ");
		scanf("%s", nova_palavra);
		for (int i = 0; i < (int)strlen(nova_palavra); i++) {
			nova_palavra[i] = toupper(nova_palavra[i]);
		}

		FILE *f;
		f = fopen("palavras.txt", "r+");
		if (f == 0) {
			printf("Sem dados.");
			exit(1);
		}
		
		int qtd;
		fscanf(f, "%d", &qtd);
		qtd++;
		fseek(f, 0, SEEK_SET);
		fprintf(f, "%d", qtd);

		fseek(f, 0, SEEK_END);
		fprintf(f, "\n%s", nova_palavra);

		fclose(f);
	}
}

void escolhe_palavra() {
	FILE* f;
	
	f = fopen("palavras.txt", "r");
	if (f == 0) {
		printf("Sem dados.");
		exit(1);
	}

	int qtd_palavras;
	fscanf(f, "%d", &qtd_palavras);

	printf("\n%d\n", qtd_palavras);

	srand(time(0));
	int random = rand() % qtd_palavras + 1;

	for (int i = 0; i < random; i++) {
		fscanf(f, "%s", palavra_secreta);
	}

	fclose(f);
}


int main() {

	escolhe_palavra();
    
	opening();

	do {	
		printf("Voce chutou %d vezes.\n", chutes_dados);

		desenha_forca();
		chuta();

	} while (!acertou() && !enforcou());

	if (acertou()) {
        printf("\nParabéns, você ganhou!\n\n");

        printf("       ___________      \n");
        printf("      '._==_==_=_.'     \n");
        printf("      .-\\:      /-.    \n");
        printf("     | (|:.     |) |    \n");
        printf("      '-|:.     |-'     \n");
        printf("        \\::.    /      \n");
        printf("         '::. .'        \n");
        printf("           ) (          \n");
        printf("         _.' '._        \n");
        printf("        '-------'       \n\n");

    } else {
        printf("\nPuxa, você foi enforcado!\n");
        printf("A palavra era **%s**\n\n", palavra_secreta);

        printf("    _______________         \n");
        printf("   /               \\       \n"); 
        printf("  /                 \\      \n");
        printf("//                   \\/\\  \n");
        printf("\\|   XXXX     XXXX   | /   \n");
        printf(" |   XXXX     XXXX   |/     \n");
        printf(" |   XXX       XXX   |      \n");
        printf(" |                   |      \n");
        printf(" \\__      XXX      __/     \n");
        printf("   |\\     XXX     /|       \n");
        printf("   | |           | |        \n");
        printf("   | I I I I I I I |        \n");
        printf("   |  I I I I I I  |        \n");
        printf("   \\_             _/       \n");
        printf("     \\_         _/         \n");
        printf("       \\_______/           \n");
    }

	adiciona_palavra();

    return 0;
}
