#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int main() {
   
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

  
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> busy;
    
   
    priority_queue<int, vector<int>, greater<int>> available;

    int devices_used = 0;
    vector<int> assigned(n);

    for (int i = 0; i < n; ++i) {
        long long a, d;
        cin >> a >> d;

       
        while (!busy.empty() && busy.top().first <= a) {
            available.push(busy.top().second);
            busy.pop();
        }

        int chosen_device;
        if (!available.empty()) {
            chosen_device = available.top();
            available.pop();
        } else {
            ++devices_used;
            chosen_device = devices_used;
        }

        assigned[i] = chosen_device;
        
        busy.push({a + d + k, chosen_device});
    }
    for (int i = 0; i < n; ++i) {
        cout << assigned[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n" << devices_used << "\n";

    return 0;
}