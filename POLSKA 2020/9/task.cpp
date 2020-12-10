#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

    ifstream file;
    file.open("input.txt");

    int numbers[10000];
    
    for(int i = 0; i < 10000; i++) {
        file >> numbers[i];
    }

    int maxLength = 0;
    int maxStart;

    for(int starting = 0; starting < 10000; starting++) {
        int length = 1;
        int ending = starting + 1;

        while(numbers[ending] >= numbers[ending-1]) {
            length += 1;
            ending += 1;
        }

        if(length > maxLength) {
            maxLength = length;
            maxStart = starting;
        }

    }

    cout << maxStart << ": " << numbers[maxStart] << " - " << maxLength << endl;

    return 0;
}