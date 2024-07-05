# include <stdio.h>
# include <stdlib.h>
# include "foge.h"

int linhas;
int colunas;
char **mapa;

void free_mapa() {
    for (int i = 0; i < linhas; i++) {
        free(mapa[i]);
    }
    free(mapa);
}

void aloca_mapa() {
    mapa = malloc(sizeof(char*) * linhas);
    for (int i = 0; i < linhas; i++) {
        mapa[i] = malloc(sizeof(char) * (colunas+1));
    }
}

void le_mapa() {
    FILE *f;
    f = fopen("mapa.txt", "r");
    if (f == 0) {
        printf("Vazio.");
        exit(1);
    }

    fscanf(f, "%d %d", &linhas, &colunas);

    aloca_mapa();

    for (int i = 0; i < 5; i++) {
        fscanf(f, "%s", mapa[i]);
    }

    fclose(f);
}


int main() {

    le_mapa();

    for (int i = 0; i < 5; i++) {
        printf("%s\n", mapa[i]);
    }

    free_mapa();

    return 0;
}
