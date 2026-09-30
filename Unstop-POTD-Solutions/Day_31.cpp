#include <stdio.h>
#include <stdlib.h>

int max_collapsing_realities(int N, int M, int K,
                             const int* unstable_realities,
                             const int (*dependencies)[2]) {

    int *indegree = (int *)calloc(N, sizeof(int));
    int *unstable = (int *)calloc(N, sizeof(int));
    int *triggered = (int *)calloc(N, sizeof(int));

    /* Adjacency list: B -> A */
    int *head = (int *)malloc(N * sizeof(int));
    int *to = (int *)malloc(M * sizeof(int));
    int *next = (int *)malloc(M * sizeof(int));

    for (int i = 0; i < N; i++) head[i] = -1;

    int edge_idx = 0;

    for (int i = 0; i < M; i++) {
        int A = dependencies[i][0];
        int B = dependencies[i][1];

        to[edge_idx] = A;
        next[edge_idx] = head[B];
        head[B] = edge_idx++;

        indegree[A]++;
    }

    for (int i = 0; i < K; i++) {
        unstable[unstable_realities[i]] = 1;
    }

    int *remaining = (int *)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        remaining[i] = indegree[i];
    }

    int *queue = (int *)malloc(N * sizeof(int));
    int front = 0, rear = 0;

    /* Initially collapsible unstable realities */
    for (int i = 0; i < N; i++) {
        if (unstable[i] && remaining[i] == 0) {
            queue[rear++] = i;
        }
    }

    int collapsed = 0;

    while (front < rear) {
        int u = queue[front++];
        collapsed++;

        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];

            remaining[v]--;
            triggered[v] = 1;

            if (remaining[v] == 0 &&
                (unstable[v] || triggered[v])) {
                queue[rear++] = v;
            }
        }
    }

    free(indegree);
    free(unstable);
    free(triggered);
    free(head);
    free(to);
    free(next);
    free(remaining);
    free(queue);

    return collapsed;
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int K;
    scanf("%d", &K);

    int* unstable_realities = (int*)malloc(K * sizeof(int));
    for (int i = 0; i < K; ++i) {
        scanf("%d", &unstable_realities[i]);
    }

    int (*dependencies)[2] = (int(*)[2])malloc(M * sizeof(int[2]));
    for (int i = 0; i < M; ++i) {
        scanf("%d %d", &dependencies[i][0], &dependencies[i][1]);
    }

    int result = max_collapsing_realities(
        N, M, K, unstable_realities, dependencies
    );

    printf("%d\n", result);

    free(unstable_realities);
    free(dependencies);

    return 0;
}