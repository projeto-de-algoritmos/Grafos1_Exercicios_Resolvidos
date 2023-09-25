#include <stdio.h>
#include <string.h>

#define MAX 1000

int N, grafo[MAX][MAX], visitado[MAX], tempo[MAX];

int DFS(int u) {
    if (visitado[u] == 1) return -1; // Detecta um ciclo

    if (visitado[u] == 2) return tempo[u];

    visitado[u] = 1;
    int maxChildTime = 0;
    for (int v = 0; v < N; v++) {
        if (grafo[u][v]) {
            int childTime = DFS(v);
            if (childTime == -1) return -1; // Ciclo detectado
            if (childTime > maxChildTime) maxChildTime = childTime;
        }
    }
    visitado[u] = 2;
    tempo[u] = maxChildTime + 1;
    return tempo[u];
}

int main() {
    while (scanf("%d", &N) != EOF) {
        memset(grafo, 0, sizeof(grafo));
        memset(visitado, 0, sizeof(visitado));
        memset(tempo, 0, sizeof(tempo));

        for (int u = 0; u < N; u++) {
            int M;
            scanf("%d", &M);
            for (int j = 0; j < M; j++) {
                int v;
                scanf("%d", &v);
                grafo[u][v - 1] = 1;
            }
        }

        int maxTempo = -1;
        int possible = 1; // Variável de controle para verificar se é possível compilar
        for (int u = 0; u < N; u++) {
            if (visitado[u] == 0) {
                int result = DFS(u);
                if (result == -1) {
                    possible = 0; // Marca que não é possível compilar
                    break;
                }
                if (result > maxTempo) maxTempo = result;
            }
        }

        if (possible) {
            printf("%d\n", maxTempo);
        } else {
            printf("-1\n"); // Não é possível compilar
        }
    }

    return 0;
}
