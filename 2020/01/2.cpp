#include <iostream>
#include <fstream>

using namespace std;

int main() {

    ifstream file;
    file.open("input.txt");

    int numbers[200];

    for(int i = 0; i < 200; i++) {
        file >> numbers[i];
    }

    for(int i = 0; i < 200; i++) {
        for(int j = i; j < 200; j++) {
            for(int k = j; k < 200; k++) {
                if(numbers[i] + numbers[j] + numbers[k] == 2020) {
                    cout << numbers[i] * numbers[j] * numbers[k] << endl;
                    return 0;
                }
            }
        }
    }
    

    return 0;
}