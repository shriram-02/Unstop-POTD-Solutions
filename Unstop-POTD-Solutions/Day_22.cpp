#include <iostream>
#include <string>
#include <vector>
#include <climits>

int shortest_substring_length(const std::string &S, const std::string &L) {
    // Frequency arrays for ASCII characters
    std::vector<int> need(256, 0);
    std::vector<int> window(256, 0);

    // Store required character frequencies
    for (char c : L) {
        need[(unsigned char)c]++;
    }

    int required = 0;
    for (int i = 0; i < 256; i++) {
        if (need[i] > 0)
            required++;
    }

    int formed = 0;
    int left = 0;
    int minLen = INT_MAX;

    // Sliding window
    for (int right = 0; right < S.size(); right++) {
        char c = S[right];
        window[(unsigned char)c]++;

        // Check if current character satisfies required frequency
        if (need[(unsigned char)c] > 0 &&
            window[(unsigned char)c] == need[(unsigned char)c]) {
            formed++;
        }

        // Try shrinking the window
        while (left <= right && formed == required) {
            minLen = std::min(minLen, right - left + 1);

            char leftChar = S[left];
            window[(unsigned char)leftChar]--;

            if (need[(unsigned char)leftChar] > 0 &&
                window[(unsigned char)leftChar] < need[(unsigned char)leftChar]) {
                formed--;
            }

            left++;
        }
    }

    return (minLen == INT_MAX) ? -1 : minLen;
}

int main() {
    std::string S;
    std::string L;

    std::getline(std::cin, S);
    std::getline(std::cin, L);

    // Call user logic function and print the output
    int result = shortest_substring_length(S, L);
    std::cout << result << std::endl;

    return 0;
}