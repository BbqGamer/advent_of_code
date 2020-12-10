#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool answers[26];

void zeros(bool * tab, int len) {
    for(int i = 0; i < len; i++) {
        tab[i] = 0;
    }
}

int countTab(bool * tab, int len) {
    int count = 0;
    for(int i = 0; i < len; i++) {
        count += tab[i];
    }
    return count;
}

int main() {

    ifstream file;
    file.open("input.txt");

    string str;
    int sum = 0;

    while(getline(file, str)) {
        if(str == "") {
            sum += countTab(answers, 26);
            zeros(answers, 26);
        } else {
            for(int i = 0; i < str.length(); i++) {
                answers[str[i]-97] = 1;
            }
        }
    }

    cout << sum;

    return 0;
}