#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int max_chocolates(vector<vector<int>>& grid, int n, int m) {
    // 3D DP: dp[row][col1][col2] = max chocolates robots can collect
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(m, -1)));

    // Base case: last row
    for (int j1 = 0; j1 < m; j1++) {
        for (int j2 = 0; j2 < m; j2++) {
            if (j1 == j2) dp[n-1][j1][j2] = grid[n-1][j1];
            else dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2];
        }
    }

    // Fill DP from bottom up
    for (int i = n-2; i >= 0; i--) {
        for (int j1 = 0; j1 < m; j1++) {
            for (int j2 = 0; j2 < m; j2++) {
                int maxi = -1e9;
                // Explore all 9 moves (robot1: -1,0,+1 ; robot2: -1,0,+1)
                for (int d1 = -1; d1 <= 1; d1++) {
                    for (int d2 = -1; d2 <= 1; d2++) {
                        int nj1 = j1 + d1;
                        int nj2 = j2 + d2;
                        if (nj1 >= 0 && nj1 < m && nj2 >= 0 && nj2 < m) {
                            int value = 0;
                            if (j1 == j2) value = grid[i][j1];
                            else value = grid[i][j1] + grid[i][j2];
                            value += dp[i+1][nj1][nj2];
                            maxi = max(maxi, value);
                        }
                    }
                }
                dp[i][j1][j2] = maxi;
            }
        }
    }

    return dp[0][0][m-1];
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }
    int result = max_chocolates(grid, n, m);
    cout << result << endl;
    return 0;
}