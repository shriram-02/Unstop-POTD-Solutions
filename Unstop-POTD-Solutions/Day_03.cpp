#include <iostream>
#include <vector>
#include <unordered_map>
#include <map>
#include <string>
using namespace std;

int longestBalancedFrequencySubarray(const vector<int>& arr) {
    int n = arr.size();
    int maxLen = 0;

    for (int i = 0; i < n; i++) {
        unordered_map<int, int> freq;

        for (int j = i; j < n; j++) {
            freq[arr[j]]++;

            int val = -1;
            bool ok = true;

            for (auto &p : freq) {
                if (val == -1) val = p.second;
                else if (p.second != val) {
                    ok = false;
                    break;
                }
            }

            if (ok) {
                maxLen = max(maxLen, j - i + 1);
            }
        }
    }

    return maxLen;
}

int main() {
    int n;
    cin >> n; // Read the size of the array

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i]; // Read the array elements
    }

    // Call user logic function and print the output
    int result = longestBalancedFrequencySubarray(arr);
    cout << result << endl;

    return 0;
}