#include <stdio.h>
#include <stdlib.h>

typedef struct {
    long long id;
    int freq;
} Book;

int cmp(const void *a, const void *b) {
    long long x = (*(Book *)a).id;
    long long y = (*(Book *)b).id;

    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int main() {
    int N;
    scanf("%d", &N);

    Book *books = (Book *)malloc(N * sizeof(Book));

    for (int i = 0; i < N; i++) {
        scanf("%lld", &books[i].id);
        books[i].freq = 0;
    }

    qsort(books, N, sizeof(Book), cmp);

    long long answer = books[0].id;
    int maxFreq = 1;

    int count = 1;

    for (int i = 1; i < N; i++) {
        if (books[i].id == books[i - 1].id) {
            count++;
        } else {
            if (count > maxFreq || (count == maxFreq && books[i - 1].id < answer)) {
                maxFreq = count;
                answer = books[i - 1].id;
            }
            count = 1;
        }
    }

    /* Check last group */
    if (count > maxFreq || (count == maxFreq && books[N - 1].id < answer)) {
        answer = books[N - 1].id;
    }

    printf("%lld\n", answer);

    free(books);
    return 0;
}