#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXQ 200005

typedef struct {
    int type;  
    int id;
    int sev;
} Event;

typedef struct {
    int severity;
    int order;
    int idx;
    int version;
} HeapNode;

static Event events[MAXQ];
static int allIds[MAXQ];
static int allCnt = 0;

static int idValues[MAXQ];
static int waiting[MAXQ];
static int curSeverity[MAXQ];
static int arrivalOrder[MAXQ];
static int versionArr[MAXQ];

static HeapNode heap[MAXQ];
static int heapSize = 0;

static int better(HeapNode a, HeapNode b) {
    if (a.severity != b.severity)
        return a.severity > b.severity;
    return a.order < b.order;
}

static void heapPush(HeapNode x) {
    int i = heapSize++;
    heap[i] = x;

    while (i > 0) {
        int p = (i - 1) / 2;
        if (!better(heap[i], heap[p]))
            break;

        HeapNode tmp = heap[i];
        heap[i] = heap[p];
        heap[p] = tmp;
        i = p;
    }
}

static void heapPop(void) {
    heapSize--;

    if (heapSize <= 0)
        return;

    heap[0] = heap[heapSize];

    int i = 0;
    while (1) {
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        int best = i;

        if (l < heapSize && better(heap[l], heap[best]))
            best = l;
        if (r < heapSize && better(heap[r], heap[best]))
            best = r;

        if (best == i)
            break;

        HeapNode tmp = heap[i];
        heap[i] = heap[best];
        heap[best] = tmp;
        i = best;
    }
}

static int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

static int mapId(int id, int M) {
    int l = 0, r = M - 1;

    while (l <= r) {
        int m = (l + r) / 2;

        if (idValues[m] == id)
            return m;

        if (idValues[m] < id)
            l = m + 1;
        else
            r = m - 1;
    }

    return -1;
}

int main(void) {
    int Q;
    scanf("%d", &Q);

    for (int i = 0; i < Q; i++) {
        char op[16];
        scanf("%s", op);

        if (strcmp(op, "ARRIVE") == 0) {
            int id, sev;
            scanf("%d %d", &id, &sev);

            events[i].type = 0;
            events[i].id = id;
            events[i].sev = sev;

            allIds[allCnt++] = id;
        } else if (strcmp(op, "REPORT") == 0) {
            int id, sev;
            scanf("%d %d", &id, &sev);

            events[i].type = 1;
            events[i].id = id;
            events[i].sev = sev;

            allIds[allCnt++] = id;
        } else if (strcmp(op, "LEAVE") == 0) {
            int id;
            scanf("%d", &id);

            events[i].type = 2;
            events[i].id = id;
            events[i].sev = 0;

            allIds[allCnt++] = id;
        } else if (strcmp(op, "CALL") == 0) {
            events[i].type = 3;
            events[i].id = 0;
            events[i].sev = 0;
        }
    }

    qsort(allIds, allCnt, sizeof(int), cmpInt);

    int M = 0;
    for (int i = 0; i < allCnt; i++) {
        if (i == 0 || allIds[i] != allIds[i - 1])
            idValues[M++] = allIds[i];
    }

    int waitingCount = 0;
    int orderCounter = 0;

    for (int i = 0; i < Q; i++) {
        int type = events[i].type;

        if (type == 0) {
            int id = events[i].id;
            int sev = events[i].sev;

            int idx = mapId(id, M);

            waiting[idx] = 1;
            curSeverity[idx] = sev;
            arrivalOrder[idx] = ++orderCounter;
            versionArr[idx]++;

            HeapNode node;
            node.severity = sev;
            node.order = arrivalOrder[idx];
            node.idx = idx;
            node.version = versionArr[idx];

            heapPush(node);
            waitingCount++;
        } else if (type == 1) { 
            int id = events[i].id;
            int sev = events[i].sev;

            int idx = mapId(id, M);

            if (idx >= 0 && waiting[idx] && sev > curSeverity[idx]) {
                curSeverity[idx] = sev;
                versionArr[idx]++;

                HeapNode node;
                node.severity = sev;
                node.order = arrivalOrder[idx];
                node.idx = idx;
                node.version = versionArr[idx];

                heapPush(node);
            }
        } else if (type == 2) { 
            int id = events[i].id;
            int idx = mapId(id, M);

            if (idx >= 0 && waiting[idx]) {
                waiting[idx] = 0;
                versionArr[idx]++;
                waitingCount--;
            }
        } else if (type == 3) { 
            while (heapSize > 0) {
                HeapNode top = heap[0];

                if (waiting[top.idx] &&
                    versionArr[top.idx] == top.version &&
                    curSeverity[top.idx] == top.severity) {
                    break;
                }

                heapPop();
            }

            if (heapSize == 0) {
                printf("NONE\n");
            } else {
                HeapNode top = heap[0];

                printf("%d\n", idValues[top.idx]);

                waiting[top.idx] = 0;
                versionArr[top.idx]++;
                waitingCount--;

                heapPop();
            }
        }
    }

    printf("Waiting: %d\n", waitingCount);

    return 0;
}