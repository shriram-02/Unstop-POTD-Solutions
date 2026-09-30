#include <stdio.h>
#include <string.h>

#define MAX 1000

int n, m;
char grid[MAX][MAX];
int visited[MAX][MAX];

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void dfs(int x, int y) {
    visited[x][y] = 1;

    for (int k = 0; k < 4; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];

        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            if (!visited[nx][ny] && grid[nx][ny] == '1') {
                dfs(nx, ny);
            }
        }
    }
}

// Function where the user will write their logic
int min_operations_to_turn_off(int n_input, int m_input, char g[MAX][MAX]) {
    n = n_input;
    m = m_input;

    // copy grid
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            grid[i][j] = g[i][j];
            visited[i][j] = 0;
        }
    }

    int components = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '1' && !visited[i][j]) {
                dfs(i, j);
                components++;
            }
        }
    }

    return components;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    char grid[MAX][MAX];
    for (int i = 0; i < n; ++i) {
        scanf("%s", grid[i]);
    }

    int result = min_operations_to_turn_off(n, m, grid);
    printf("%d\n", result);

    return 0;
}