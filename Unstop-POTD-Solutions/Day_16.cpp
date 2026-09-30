#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long ans = 0;

/*
tree indexing:
node v
left child  = 2*v
right child = 2*v + 1

weights[i-2] stores weight of edge:
i -> floor(i/2)
*/

long long dfs(int node, int maxNode, const vector<int>& weights) {
    // leaf node
    if (2 * node > maxNode) {
        return 0;
    }

    int left = 2 * node;
    int right = 2 * node + 1;

    long long leftPath =
        dfs(left, maxNode, weights) + weights[left - 2];

    long long rightPath =
        dfs(right, maxNode, weights) + weights[right - 2];

    ans += abs(leftPath - rightPath);

    return max(leftPath, rightPath);
}

int user_logic(int n, const std::vector<int>& weights) {
    ans = 0;

    int totalNodes = (1 << (n + 1)) - 1;

    dfs(1, totalNodes, weights);

    return ans;
}

int main() {
    int n;
    cin >> n;

    vector<int> weights((1 << (n + 1)) - 2);

    for (int i = 0; i < weights.size(); ++i) {
        cin >> weights[i];
    }

    int result = user_logic(n, weights);

    cout << result << endl;

    return 0;
}