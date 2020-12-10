#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int answers[26];

void zeros(int * tab, int len) {
    for(int i = 0; i < len; i++) {
        tab[i] = 0;
    }
}

int countTab(int * tab, int len, int numberOfPeople) {
    int count = 0;
    for(int i = 0; i < len; i++) {
        if(tab[i] == numberOfPeople) {
            count += 1;
        }
    }
    return count;
}

int main() {

    ifstream file;
    file.open("input.txt");

    string str;
    int sum = 0;
    int numberOfPeople = 0;

    while(getline(file, str)) {
        if(str == "") {
            sum += countTab(answers, 26, numberOfPeople);




            zeros(answers, 26);
            numberOfPeople = 0;
        } else {
            numberOfPeople += 1;
            for(int i = 0; i < str.length(); i++) {
                answers[str[i]-97] += 1;
            }
        }
    }

    cout << sum;

    return 0;
}