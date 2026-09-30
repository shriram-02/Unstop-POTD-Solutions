#include <iostream>
#include <string>

int LongestConsecutiveCharacter(const std::string& s) {
    // If string is empty
    if (s.empty()) {
        return 0;
    }

    int maxLength = 1;
    int currentLength = 1;

    // Traverse the string
    for (int i = 1; i < s.length(); i++) {
        if (s[i] == s[i - 1]) {
            currentLength++;
        } else {
            currentLength = 1;
        }

        // Update maximum length
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }
    }

    return maxLength;
}

int main() {
    std::string s;
    std::getline(std::cin, s);
    
    // Call user logic function and print the output
    int result = LongestConsecutiveCharacter(s);
    std::cout << result << std::endl;
    
    return 0;
}