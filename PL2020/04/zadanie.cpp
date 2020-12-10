#include <iostream>
#include <fstream>

int occurences[1000];

using namespace std;

int main() {

    ifstream file;
    file.open("input.txt");

    int number;
  
    while(file >> number) {
        occurences[number] += 1;
    }

    int max = 0;
    int maxI;

    for(int i = 0; i < 1000; i++) {
        if(occurences[i] > max) {
            max = occurences[i];
            maxI = i;
        }
    }

    cout << max << endl;
    cout << maxI << endl;

    return 0;
}