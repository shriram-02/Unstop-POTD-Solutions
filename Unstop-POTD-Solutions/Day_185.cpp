#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    long long D;
    cin >> N >> D >> M;

    vector<int> s(N);
    vector<long long> w(N);

    for (int i = 0; i < N; i++) {
        cin >> s[i] >> w[i];
    }

    unordered_map<int, int> freq;

    deque<int> mn, mx;

    int left = 0;
    int bestLen = 0;
    int bestStart = 1;

    for (int right = 0; right < N; right++) {

        freq[s[right]]++;

        while (!mn.empty() && w[mn.back()] >= w[right])
            mn.pop_back();
        mn.push_back(right);

        while (!mx.empty() && w[mx.back()] <= w[right])
            mx.pop_back();
        mx.push_back(right);

        while (w[mx.front()] - w[mn.front()] > D ||
               freq[s[right]] > M) {

            freq[s[left]]--;

            if (freq[s[left]] == 0)
                freq.erase(s[left]);

            if (mn.front() == left)
                mn.pop_front();

            if (mx.front() == left)
                mx.pop_front();

            left++;
        }

        int len = right - left + 1;

        if (len > bestLen) {
            bestLen = len;
            bestStart = left + 1;
        }
    }

    cout << bestLen << " " << bestStart << '\n';

    return 0;
}