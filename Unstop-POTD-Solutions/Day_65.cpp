#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <set>
using namespace std;

int smallestMaxDifference(const vector<int>& arr, int k) {
    multiset<int> window;
    int minDiff = INT_MAX;

    // Initialize the first window
    for (int i = 0; i < k; ++i) {
        window.insert(arr[i]);
    }

    // Calculate the difference for the first window
    minDiff = min(minDiff, *window.rbegin() - *window.begin());

    // Slide the window
    for (int i = k; i < arr.size(); ++i) {
        // Remove the element going out of the window
        window.erase(window.find(arr[i - k]));
        // Add the new element
        window.insert(arr[i]);
        // Update the minimum difference
        minDiff = min(minDiff, *window.rbegin() - *window.begin());
    }

    return minDiff;
}

int main() {
    int n, k;
    cin >> n; // Number of elements in the array
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i]; // Input array
    }
    cin >> k; // Size of the subarray

    cout << smallestMaxDifference(arr, k) << endl;

    return 0;
}