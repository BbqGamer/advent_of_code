#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

    ifstream file;
    file.open("input.txt");

    int number;
  
    for(int i = 0; i < 3; i++) {
        file >> number;
        cout << number << endl;
    }

    return 0;
}