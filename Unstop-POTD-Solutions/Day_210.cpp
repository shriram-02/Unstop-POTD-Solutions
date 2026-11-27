#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    cin >> m;

    unordered_map<long long, long long> values;
    vector<unordered_map<long long, long long>> history(1);
    vector<long long> output;

    long long total = 0;

    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;

        if (s == "B") {
            history.push_back({});
        }
        else if (s == "D") {
            for (auto &p : history.back()) {
                long long k = p.first;
                long long oldValue = p.second;

                if (values.count(k))
                    total -= values[k];

                if (oldValue == -1)
                    values.erase(k);
                else {
                    values[k] = oldValue;
                    total += oldValue;
                }
            }
            history.pop_back();
        }
        else if (s == "K") {
            auto changes = history.back();
            history.pop_back();

            if (!history.empty()) {
                for (auto &p : changes) {
                    if (!history.back().count(p.first))
                        history.back()[p.first] = p.second;
                }
            }
        }
        else if (s[0] == 'S') {
            int pos = s.find('=');
            long long k = stoll(s.substr(1, pos - 1));
            long long v = stoll(s.substr(pos + 1));

            if (!history.back().count(k)) {
                history.back()[k] = values.count(k) ? values[k] : -1;
            }

            if (values.count(k))
                total -= values[k];

            values[k] = v;
            total += v;
        }
        else if (s[0] == 'G') {
            long long k = stoll(s.substr(1));
            output.push_back(values.count(k) ? values[k] : -1);
        }
        else if (s == "T") {
            output.push_back(total);
        }
    }

    for (int i = 0; i < (int)output.size(); i++) {
        if (i) cout << " ";
        cout << output[i];
    }

    cout << "\n";
    return 0;
}