#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

    ifstream file;
    file.open("input.txt");

    int min;
    int max;
    char buffor;
    char letter;
    string password;
    int numberOfValid = 0;

    while(file >> min) {
        file >> buffor;
        file >> max;
        file >> letter;
        file >> buffor;
        file >> password;

        int letterCount = 0;
        for(int i = 0; i < password.length(); i++) {
            if(password[i] == letter) {
                letterCount += 1;
            }
        }

        if(letterCount >= min && letterCount <= max) {
            numberOfValid += 1;
        }
    }

    cout << numberOfValid;

    return 0;
}