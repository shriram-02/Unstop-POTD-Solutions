#include <stdio.h>
#include <stdlib.h>

#define MAXN 100005
#define LOG 18
#define MAXNODE 2000005

static int head[MAXN], to[2 * MAXN], nxt[2 * MAXN], ec;
static int up[LOG][MAXN], depth[MAXN], root[MAXN];
static int order[MAXN];

static long long levy[MAXN], vals[MAXN];

static int lc[MAXNODE], rc[MAXNODE], cnt[MAXNODE], nodes;
static long long sum[MAXNODE];

static int m;

void addEdge(int a, int b) {
    to[++ec] = b;
    nxt[ec] = head[a];
    head[a] = ec;
}

int compare(const void *a, const void *b) {
    long long x = *(const long long *)a;
    long long y = *(const long long *)b;
    return (x > y) - (x < y);
}

int insert(int old, int l, int r, int pos, long long value) {
    int id = ++nodes;

    lc[id] = lc[old];
    rc[id] = rc[old];
    cnt[id] = cnt[old] + 1;
    sum[id] = sum[old] + value;

    if (l != r) {
        int mid = (l + r) / 2;

        if (pos <= mid)
            lc[id] = insert(lc[old], l, mid, pos, value);
        else
            rc[id] = insert(rc[old], mid + 1, r, pos, value);
    }

    return id;
}

long long largest(int a, int b, int l, int r, int k) {
    int count = cnt[a] - cnt[b];

    if (k <= 0)
        return 0;

    if (k >= count)
        return sum[a] - sum[b];

    if (l == r)
        return (long long)k * vals[l - 1];

    int mid = (l + r) / 2;

    int ra = rc[a];
    int rb = rc[b];

    int rightCount = cnt[ra] - cnt[rb];

    if (k <= rightCount)
        return largest(ra, rb, mid + 1, r, k);

    return sum[ra] - sum[rb] +
           largest(lc[a], lc[b], l, mid, k - rightCount);
}

long long getCost(int u, int v, int k) {
    int a = up[0][u];
    int b = up[0][v];

    long long total = sum[root[a]] - sum[root[b]];

    long long saved = largest(
        root[a], root[b], 1, m, k
    );

    return total - saved;
}

int main() {
    int n, q;

    if (scanf("%d %d", &n, &q) != 2)
        return 0;

    for (int i = 1; i <= n; i++) {
        scanf("%lld", &levy[i]);
        vals[i - 1] = levy[i];
    }

    qsort(vals, n, sizeof(long long), compare);

    m = 0;

    for (int i = 0; i < n; i++) {
        if (i == 0 || vals[i] != vals[i - 1])
            vals[m++] = vals[i];
    }

    for (int i = 1; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);

        addEdge(a, b);
        addEdge(b, a);
    }

    int front = 0, back = 0;

    order[back++] = 1;
    depth[1] = 0;

    while (front < back) {
        int u = order[front++];

        for (int e = head[u]; e; e = nxt[e]) {
            int v = to[e];

            if (v == up[0][u])
                continue;

            up[0][v] = u;
            depth[v] = depth[u] + 1;

            order[back++] = v;
        }
    }

    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= n; i++) {
            up[j][i] = up[j - 1][up[j - 1][i]];
        }
    }

    for (int i = 0; i < n; i++) {
        int u = order[i];

        int lo = 0, hi = m - 1;

        while (lo < hi) {
            int mid = (lo + hi) / 2;

            if (vals[mid] < levy[u])
                lo = mid + 1;
            else
                hi = mid;
        }

        root[u] = insert(
            root[up[0][u]],
            1, m, lo + 1, levy[u]
        );
    }

    while (q--) {
        int u, k;
        long long B;

        scanf("%d %lld %d", &u, &B, &k);

        int v = u;

        for (int j = LOG - 1; j >= 0; j--) {
            int ancestor = up[j][v];

            if (ancestor != 0 &&
                getCost(u, ancestor, k) <= B) {
                v = ancestor;
            }
        }

        printf("%d %lld\n", v, getCost(u, v, k));
    }

    return 0;
}