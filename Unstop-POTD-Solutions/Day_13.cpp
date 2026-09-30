#include <iostream>
#include <string>

using namespace std;

// User logic function
string canMakeHalvesEqual(const string& S) {
    int n = S.length() / 2;

    int firstZero = 0, secondZero = 0;

    // Count zeros in first half
    for (int i = 0; i < n; i++) {
        if (S[i] == '0')
            firstZero++;
    }

    // Count zeros in second half
    for (int i = n; i < 2 * n; i++) {
        if (S[i] == '0')
            secondZero++;
    }

    // If counts match, rearrangement is possible
    if (firstZero == secondZero)
        return "YES";

    return "NO";
}

int main() {
    string S;
    cin >> S;

    // Call the user logic function and print the result
    string result = canMakeHalvesEqual(S);
    cout << result << endl;

    return 0;
}