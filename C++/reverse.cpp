#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// #include <stdio.h>

class Solution {
public:
    void reverseString(vector<char>& s) {
        char temp;
        int n = s.size(); // only accessing it once decreases the runtime by 4ms
        for(int i = 0; i < n/2; ++i) {
            temp = s[i];
            s[i] = s[n - 1 - i];
            s[n - 1 - i] = temp;
        }
    }
};

int main(int argc, char *argv[]){
    Solution s = Solution();
    vector<char> str {'s', 't', 'r'};
    s.reverseString(str);
    for(char i: str){
        cout << i;
    }
}