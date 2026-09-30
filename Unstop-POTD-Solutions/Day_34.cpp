#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int count_divisible_subarrays(int n, int k, const vector<int>& arr) {
    const long long MOD = 1000000007LL;

    unordered_map<long long, long long> freq;
    freq[0] = 1;

    long long pref = 0;
    long long ans = 0;

    for (int i = 0; i < n; i++) {
        pref += arr[i];

        long long rem = ((pref % k) + k) % k;

        ans = (ans + freq[rem]) % MOD;
        freq[rem]++;
    }

    return (int)(ans % MOD);
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << count_divisible_subarrays(n, k, arr) << endl;

    return 0;
}