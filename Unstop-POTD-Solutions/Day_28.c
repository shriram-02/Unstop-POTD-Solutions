#include <stdio.h>

void compute_max_intensity_after_k_hours(int N, int intensities[], int K, int queries[][2], int Q) {

    int curr[N], next[N];

    // Copy initial intensities
    for (int i = 0; i < N; i++) {
        curr[i] = intensities[i];
    }

    // Simulate for K hours
    for (int hour = 0; hour < K; hour++) {

        // If only one city
        if (N == 1) {
            next[0] = curr[0];
        } else {

            // First city
            next[0] = curr[1];

            // Middle cities
            for (int i = 1; i < N - 1; i++) {
                next[i] = (curr[i - 1] + curr[i + 1]) / 2;
            }

            // Last city
            next[N - 1] = curr[N - 2];
        }

        // Update current array
        for (int i = 0; i < N; i++) {
            curr[i] = next[i];
        }
    }

    // Process queries
    for (int q = 0; q < Q; q++) {

        int l = queries[q][0] - 1;
        int r = queries[q][1] - 1;

        int max_value = curr[l];

        for (int i = l + 1; i <= r; i++) {
            if (curr[i] > max_value) {
                max_value = curr[i];
            }
        }

        printf("%d\n", max_value);
    }
}

int main() {

    int N;
    scanf("%d", &N);

    int intensities[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &intensities[i]);
    }

    int K;
    scanf("%d", &K);

    int Q;
    scanf("%d", &Q);

    int queries[Q][2];

    for (int i = 0; i < Q; i++) {
        scanf("%d %d", &queries[i][0], &queries[i][1]);
    }

    compute_max_intensity_after_k_hours(N, intensities, K, queries, Q);

    return 0;
}