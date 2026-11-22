#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;

    unordered_map<int, set<pair<int, int>>> mp;
    unordered_map<int, pair<int, int>> requests;

    while (q--) {
        string op;
        cin >> op;

        if (op == "NEW") {
            int id, ward, urgency;
            cin >> id >> ward >> urgency;

            mp[ward].insert({-urgency, id});
            requests[id] = {ward, urgency};
        }
        else if (op == "CHANGE") {
            int id, urgency;
            cin >> id >> urgency;

            int ward = requests[id].first;
            int oldUrgency = requests[id].second;

            mp[ward].erase({-oldUrgency, id});
            mp[ward].insert({-urgency, id});

            requests[id].second = urgency;
        }
        else if (op == "WITHDRAW") {
            int id;
            cin >> id;

            int ward = requests[id].first;
            int urgency = requests[id].second;

            mp[ward].erase({-urgency, id});
            requests.erase(id);
        }
        else if (op == "SERVE") {
            int ward;
            cin >> ward;

            if (mp[ward].empty()) {
                cout << "NONE\n";
            }
            else {
                auto it = mp[ward].begin();

                int urgency = -it->first;
                int id = it->second;

                cout << id << " " << urgency << "\n";

                mp[ward].erase(it);
                requests.erase(id);
            }
        }
    }

    return 0;
}