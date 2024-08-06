void free_mapa();
void aloca_mapa();
void le_mapa();

void move(char direcao);
int acabou();
void imprimemapa();

typedef struct {
    char **matriz;
    int linhas;
    int colunas;
} mapa;

// typedef struct mapa MAPA;