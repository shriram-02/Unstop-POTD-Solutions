#include <iostream>
#include <set>
#include <unordered_map>
#include <chrono>

using namespace std;

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int B, Q;
    if (!(cin >> B >> Q)) return 0;

    set<pair<long long, long long>> active_batches;
    unordered_map<long long, long long, custom_hash> counts;
    long long total_doses = 0;

    for (int i = 0; i < B; ++i) {
        long long id, exp, count;
        cin >> id >> exp >> count;
        active_batches.insert({exp, id});
        counts[id] = count;
        total_doses += count;
    }

    for (int i = 0; i < Q; ++i) {
        char type;
        cin >> type;
        if (type == 'A') {
            long long id, exp, count;
            cin >> id >> exp >> count;
            active_batches.insert({exp, id});
            counts[id] = count;
            total_doses += count;
        } else if (type == 'R') {
            long long id;
            cin >> id;
            auto it = counts.find(id);
            if (it != counts.end()) {
                total_doses -= it->second;
                it->second = 0;
            }
        } else if (type == 'I') {
            long long x;
            cin >> x;
            if (x > total_doses) {
                cout << "SHORT\n";
            } else {
                total_doses -= x;
                long long last_expiry = -1;
                long long num_batches = 0;
                
                while (x > 0) {
                    auto it = active_batches.begin();
                    long long exp = it->first;
                    long long id = it->second;
                    
                    long long c = counts[id];
                    if (c == 0) {
                        active_batches.erase(it);
                        continue;
                    }
                    
                    if (c <= x) {
                        x -= c;
                        counts[id] = 0;
                        active_batches.erase(it);
                        last_expiry = exp;
                        num_batches++;
                    } else {
                        counts[id] -= x;
                        x = 0;
                        last_expiry = exp;
                        num_batches++;
                    }
                }
                cout << last_expiry << " " << num_batches << "\n";
            }
        }
    }

    return 0;
}