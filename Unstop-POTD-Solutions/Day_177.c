#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 200005
#define HASH_SIZE 524287

typedef struct {
    char name[11];
    int reading;
    long long expiry;
    int version;
} HeapNode;

typedef struct {
    char name[11];
    int version;
} Station;

HeapNode heap[MAXN];
Station stations[MAXN];

int hashTable[HASH_SIZE];
int heapSize = 0;
int stationCount = 0;

unsigned long hashName(const char *s) {
    unsigned long h = 5381;

    while (*s) {
        h = ((h << 5) + h) + *s;
        s++;
    }

    return h % HASH_SIZE;
}

int getStation(const char *name) {
    unsigned long h = hashName(name);

    while (hashTable[h] != 0) {
        int id = hashTable[h] - 1;

        if (strcmp(stations[id].name, name) == 0)
            return id;

        h = (h + 1) % HASH_SIZE;
    }

    int id = stationCount++;

    strcpy(stations[id].name, name);
    stations[id].version = 0;

    hashTable[h] = id + 1;

    return id;
}

int better(HeapNode a, HeapNode b) {
    if (a.reading != b.reading)
        return a.reading > b.reading;

    return strcmp(a.name, b.name) < 0;
}

void push(HeapNode x) {
    int i = ++heapSize;

    while (i > 1 && better(x, heap[i / 2])) {
        heap[i] = heap[i / 2];
        i /= 2;
    }

    heap[i] = x;
}

void pop() {
    HeapNode last = heap[heapSize--];

    if (heapSize == 0)
        return;

    int i = 1;

    while (i * 2 <= heapSize) {
        int child = i * 2;

        if (child + 1 <= heapSize &&
            better(heap[child + 1], heap[child])) {
            child++;
        }

        if (!better(heap[child], last))
            break;

        heap[i] = heap[child];
        i = child;
    }

    heap[i] = last;
}

int main() {
    int N;
    long long T;

    scanf("%d %lld", &N, &T);

    for (int i = 0; i < N; i++) {
        char type;
        long long time;

        scanf(" %c %lld", &type, &time);

        if (type == 'R') {
            char name[11];
            int reading;

            scanf("%10s %d", name, &reading);

            int id = getStation(name);

            stations[id].version++;

            HeapNode node;

            strcpy(node.name, name);
            node.reading = reading;
            node.expiry = time + T;
            node.version = stations[id].version;

            push(node);
        }
        else if (type == 'Q') {

            while (heapSize > 0) {
                HeapNode top = heap[1];

                int id = getStation(top.name);

                if (top.expiry <= time ||
                    top.version != stations[id].version) {
                    pop();
                }
                else {
                    break;
                }
            }

            if (heapSize == 0) {
                printf("NONE\n");
            }
            else {
                printf("%s %d\n",
                       heap[1].name,
                       heap[1].reading);
            }
        }
    }

    return 0;
}