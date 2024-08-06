# include <stdio.h>
# include <stdlib.h>
# include "foge.h"

mapa m;

void free_mapa() {
    for (int i = 0; i < m.linhas; i++) {
        free(m.matriz[i]);
    }
    free(m.matriz);
}

void aloca_mapa() {
    m.matriz = malloc(sizeof(char*) * m.linhas);
    for (int i = 0; i < m.linhas; i++) {
        m.matriz[i] = malloc(sizeof(char) * (m.colunas+1));
    }
}

void le_mapa() {
    FILE *f;
    f = fopen("mapa.txt", "r");
    if (f == 0) {
        printf("Vazio.");
        exit(1);
    }

    fscanf(f, "%d %d", &m.linhas, &m.colunas);

    aloca_mapa();

    for (int i = 0; i < 5; i++) {
        fscanf(f, "%s", m.matriz[i]);
    }

    fclose(f);
}

void imprimemapa() {
    for (int i = 0; i < 5; i++) {
        printf("%s\n", m.matriz[i]);
    }
}

int acabou() {
    return 0;
}

void move(char direcao) {

    int x;
    int y;

    for (int i = 0; i < m.linhas; i++) {
        for (int j = 0; j < m.colunas; j++) {
            if (m.matriz[i][j] == '@') {
                x = i;
                y = j;
            }
        }
    }

    switch (direcao) {
        case 'a':
            m.matriz[x][y-1] = '@';
            break;
        case 'd':
            m.matriz[x][y+1] = '@';
            break;
        case 's':
            m.matriz[x+1][y] = '@';
            break;
        case 'w':
            m.matriz[x-1][y] = '@';
        default:
            printf("Tecla invalida.");    
    }
    m.matriz[x][y] = '.';
}

int main() {

    le_mapa();

    do {

        imprimemapa();
        
        char comando;
        scanf(" %c", &comando);
        move(comando);

    } while (!acabou());

    free_mapa();

    return 0;
}
