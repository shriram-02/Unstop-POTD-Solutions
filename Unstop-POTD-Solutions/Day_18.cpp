#include <iostream>
#include <vector>

void can_select_people(int N, int K, std::vector<int>& arr) {
    // dp[i] = true if sum i can be formed
    std::vector<bool> dp(K + 1, false);
    
    dp[0] = true; // Base case
    
    for (int i = 0; i < N; ++i) {
        // Traverse backwards to avoid using same element multiple times
        for (int j = K; j >= arr[i]; --j) {
            dp[j] = dp[j] || dp[j - arr[i]];
        }
    }
    
    if (dp[K]) {
        std::cout << "YES";
    } else {
        std::cout << "NO";
    }
}

int main() {
    int N, K;
    std::cin >> N >> K;

    std::vector<int> arr(N);

    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    can_select_people(N, K, arr);

    return 0;
}