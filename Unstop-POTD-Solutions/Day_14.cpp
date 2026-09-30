#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int minRefuels(int N, int M, int D, int S, int E, vector<vector<int>> &flights) {
    
    // Adjacency list: {next_city, distance}
    vector<vector<pair<int, int>>> graph(N + 1);

    for (auto &f : flights) {
        int u = f[0];
        int v = f[1];
        int dist = f[2];

        // Ignore impossible flights
        if (dist <= D) {
            graph[u].push_back({v, dist});
        }
    }

    // dist[node][fuel_used] is not feasible due to constraints.
    // We use BFS/Dijkstra style:
    // state = {refuels, city, remaining_fuel}

    // For each city, store maximum remaining fuel seen
    vector<int> bestFuel(N + 1, -1);

    priority_queue<
        tuple<int, int, int>,
        vector<tuple<int, int, int>>,
        greater<tuple<int, int, int>>
    > pq;

    // Start with full tank and 0 refuels
    pq.push({0, S, D});

    while (!pq.empty()) {
        auto [refuels, city, fuel] = pq.top();
        pq.pop();

        // Destination reached
        if (city == E) {
            return refuels;
        }

        // If this state is worse, skip
        if (fuel <= bestFuel[city]) continue;
        bestFuel[city] = fuel;

        for (auto &[nextCity, dist] : graph[city]) {

            // Case 1: Fly without refueling
            if (fuel >= dist) {
                pq.push({refuels, nextCity, fuel - dist});
            }

            // Case 2: Refuel at current city first
            // (Not needed at source because already full)
            if (city != S && D >= dist) {
                pq.push({refuels + 1, nextCity, D - dist});
            }
        }
    }

    return -1;
}

int main() {
    int N, M, D;
    cin >> N >> M >> D;

    int S, E;
    cin >> S >> E;

    vector<vector<int>> flights(M, vector<int>(3));

    for (int i = 0; i < M; ++i) {
        cin >> flights[i][0] >> flights[i][1] >> flights[i][2];
    }

    int result = minRefuels(N, M, D, S, E, flights);

    cout << result << endl;

    return 0;
}