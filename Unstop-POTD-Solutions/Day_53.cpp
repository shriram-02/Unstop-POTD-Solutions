#include <iostream>
#include <vector>
#include <string>
using namespace std;

string raceWinner(int n, vector<int>& tw) {
    int tortoiseTime = n - 1;

    int rabbitTime = 0;
    int rabbitPos = 0;
    vector<bool> visited(n, false);  // Track triggered traps or delays

    while (rabbitPos < n - 1) {
        // Trap handling first
        if (tw[rabbitPos] == -1 && !visited[rabbitPos]) {
            visited[rabbitPos] = true;
            rabbitPos = max(0, rabbitPos - 1);  // Go back
            rabbitTime++;
            continue;  // Re-evaluate new position before jumping
        }

        // Delay handling
        if (tw[rabbitPos] > 0 && !visited[rabbitPos]) {
            rabbitTime += tw[rabbitPos];
            visited[rabbitPos] = true;
        }

        // Normal 2-step jump
        rabbitPos += 2;
        rabbitTime++;
    }

    if (rabbitTime < tortoiseTime) {
        return "Rabbit";
    } else if (tortoiseTime < rabbitTime) {
        return "Tortoise";
    } else {
        return "Tie";
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> tw(n);
    for (int i = 0; i < n; ++i) {
        cin >> tw[i];
    }
    string winner = raceWinner(n, tw);
    cout << winner << endl;
    return 0;
}