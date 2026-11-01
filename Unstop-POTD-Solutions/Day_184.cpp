#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

struct Gate {
    int id;
    long long max_size;
    long long turnaround;
};

struct Flight {
    long long arr;
    long long dep;
    long long size;
    int booking_index;
};

int main() {
    // Optimize standard I/O operations for speed
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int G, F;
    if (!(cin >> G >> F)) return 0;

    vector<Gate> gates(G + 1);
    set<pair<long long, int>> available_gates; // stores {max_size, id}

    for (int i = 0; i < G; ++i) {
        int id;
        long long size, turnaround;
        cin >> id >> size >> turnaround;
        gates[id] = {id, size, turnaround};
        available_gates.insert({size, id});
    }

    vector<Flight> flights(F);
    for (int i = 0; i < F; ++i) {
        cin >> flights[i].arr >> flights[i].dep >> flights[i].size;
        flights[i].booking_index = i;
    }

    // Sort flights by arrival minute, then by booking index for tie-breaking
    sort(flights.begin(), flights.end(), [](const Flight& a, const Flight& b) {
        if (a.arr != b.arr) return a.arr < b.arr;
        return a.booking_index < b.booking_index;
    });

    // Min-priority queue for busy gates: stores {avail_time, gate_id}
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> busy_gates;

    vector<int> assigned_gate(F, 0);
    vector<int> gate_handled_count(G + 1, 0);
    int success_count = 0;

    for (const auto& flight : flights) {
        // Release gates that have become available by the current flight's arrival time
        while (!busy_gates.empty() && busy_gates.top().first <= flight.arr) {
            int g_id = busy_gates.top().second;
            busy_gates.pop();
            available_gates.insert({gates[g_id].max_size, g_id});
        }

        // Find suitable gate: smallest max_size >= flight.size, then smallest id
        auto it = available_gates.lower_bound({flight.size, 0});
        if (it != available_gates.end()) {
            int g_id = it->second;
            available_gates.erase(it);

            assigned_gate[flight.booking_index] = g_id;
            gate_handled_count[g_id]++;
            success_count++;

            long long avail_time = flight.dep + gates[g_id].turnaround;
            busy_gates.push({avail_time, g_id});
        } else {
            assigned_gate[flight.booking_index] = 0; // Diverted
        }
    }

    // Determine the busiest gate
    int busiest_id = 0;
    int max_handled = 0;
    for (int i = 1; i <= G; ++i) {
        if (gate_handled_count[i] > max_handled) {
            max_handled = gate_handled_count[i];
            busiest_id = i;
        } else if (gate_handled_count[i] == max_handled && max_handled > 0) {
            if (i < busiest_id) {
                busiest_id = i;
            }
        }
    }

    // Output results
    cout << success_count << "\n";
    for (int i = 0; i < F; ++i) {
        cout << assigned_gate[i] << (i == F - 1 ? "" : " ");
    }
    cout << "\n";

    if (max_handled == 0) {
        cout << "0 0\n";
    } else {
        cout << busiest_id << " " << max_handled << "\n";
    }

    return 0;
}