#include <iostream>
#include <vector>
using namespace std;

// Function to compute the final sizes of minerals after D days
vector<long long> computeFinalSizes(int numMinerals, vector<int>& initialSizes, int numDays) {
    vector<long long> finalSizes(numMinerals);

    for (int i = 0; i < numMinerals; ++i) {
        long long size = initialSizes[i];

        // Simulate growth/shrinkage for each day
        for (int day = 1; day <= numDays; ++day) {
            if (day % 3 == 0) {
                size /= 2;   // Cooling phase every 3rd day
            } else {
                size *= 2;   // Normal growth
            }
        }

        finalSizes[i] = size;
    }

    return finalSizes;
}

int main() {
    int numMinerals, numDays;
    cin >> numMinerals;

    vector<int> initialSizes(numMinerals);

    for (int i = 0; i < numMinerals; ++i) {
        cin >> initialSizes[i];
    }

    cin >> numDays;

    // Get the final sizes of the minerals after the specified number of days
    vector<long long> result = computeFinalSizes(numMinerals, initialSizes, numDays);

    // Output the final sizes
    for (long long size : result) {
        cout << size << " ";
    }

    cout << endl;

    return 0;
}