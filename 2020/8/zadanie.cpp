#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool instructions[626];

int checkInstructionAcc(bool * instructions, string * codes, int* values, int i, int accumulator) {
    if(instructions[i] == 1) {
        return accumulator;
    } else {
        instructions[i] = 1;
        if(codes[i] == "jmp") {
            return checkInstructionAcc(instructions, codes, values, i + values[i], accumulator);
        } else if (codes[i] == "acc") {
            accumulator += values[i];
            return checkInstructionAcc(instructions, codes, values, i + 1, accumulator);
        } else {
            return checkInstructionAcc(instructions, codes, values, i + 1, accumulator);
        }
    }
}

int main() {

    ifstream file;
    file.open("input.txt");

    string codes[626];
    int values[626];
    char buffor[1];
    int value;

    string right;

    for(int i = 0; i < 626; i++) {
        file >> codes[i];
        file >> right;

        value = stoi(right.substr(1));

        if(right[0] == '-') {
            value = -value;
        }
        
        values[i] = value;
    }

    cout << checkInstructionAcc(instructions, codes, values, 0, 0) << endl;

    return 0;
}