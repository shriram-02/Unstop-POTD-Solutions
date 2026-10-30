#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;

    set<pair<long long, int>> parcels;
    unordered_map<int, long long> waiting;

    while (Q--) {
        string command;
        cin >> command;

        if (command == "ARRIVE") {
            int id;
            long long deadline;
            cin >> id >> deadline;

            parcels.insert({deadline, id});
            waiting[id] = deadline;
        }
        else if (command == "DELAY") {
            int id;
            long long deadline;
            cin >> id >> deadline;

            parcels.erase({waiting[id], id});
            parcels.insert({deadline, id});
            waiting[id] = deadline;
        }
        else if (command == "CANCEL") {
            int id;
            cin >> id;

            parcels.erase({waiting[id], id});
            waiting.erase(id);
        }
        else if (command == "DISPATCH") {
            if (parcels.empty()) {
                cout << "IDLE\n";
            }
            else {
                auto it = parcels.begin();
                int id = it->second;

                cout << id << '\n';

                parcels.erase(it);
                waiting.erase(id);
            }
        }
    }

    return 0;
}