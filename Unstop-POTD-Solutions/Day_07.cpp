#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef long long ll;

struct Node {
    ll sum;
    int start, end;
    
    bool operator<(const Node& other) const {
        return sum < other.sum; // max heap
    }
};

ll findMaxKSubarraySums(int n, int k, vector<int>& arr) {
    vector<ll> prefix(n + 1, 0);
    
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }

    priority_queue<Node> pq;

    // Initial best subarrays (start=i, end=n)
    for (int i = 0; i < n; i++) {
        ll sum = prefix[n] - prefix[i];
        pq.push({sum, i, n});
    }

    ll result = 0;

    while (k-- && !pq.empty()) {
        Node cur = pq.top();
        pq.pop();

        result += cur.sum;

        // Try shrinking from right
        if (cur.end - 1 > cur.start) {
            ll newSum = prefix[cur.end - 1] - prefix[cur.start];
            pq.push({newSum, cur.start, cur.end - 1});
        }
    }

    return result;
}

int main() {
    int n, k;
    cin >> n >> k;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << findMaxKSubarraySums(n, k, arr) << endl;
    return 0;
}