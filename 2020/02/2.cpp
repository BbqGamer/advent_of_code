#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

    ifstream file;
    file.open("input.txt");

    int first;
    int second;
    char buffor;
    char letter;
    string password;
    int numberOfValid = 0;

    while(file >> first) {
        file >> buffor;
        file >> second;
        file >> letter;
        file >> buffor;
        file >> password;

        if((password[first-1] == letter && password[second-1] != letter)||(password[first-1] != letter && password[second-1] == letter)) {
            numberOfValid += 1;
        }   
    }

    cout << numberOfValid;

    return 0;
}