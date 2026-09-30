#include <iostream>
#include <string>
#include <vector>
using namespace std;

void process_dashes(int n, string s) {
    vector<char> st;

    for (char c : s) {
        if (c == '_') {
            if (st.empty()) {
                cout << -1;
                return;
            }
            st.pop_back();
        } else {
            st.push_back(c);
        }
    }

    if (st.empty()) {
        cout << -1;
        return;
    }

    for (char c : st) {
        cout << c;
    }
}

int main() {
    int n;
    string s;

    cin >> n;
    cin >> s;

    process_dashes(n, s);

    return 0;
}