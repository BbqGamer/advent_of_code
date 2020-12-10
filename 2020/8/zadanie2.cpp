#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool instructions[626];

bool checkInstruction(bool * instructions, string * codes, int* values, int i) {
    if (i > 626) {
        return 0;
    } else if(i == 626) {
        return 1;
    } else if (instructions[i] == 1) {
        return 0;
    } else {
        instructions[i] = 1;
        if(codes[i] == "jmp") {
            return checkInstruction(instructions, codes, values, i + values[i]);
        } else {
            return checkInstruction(instructions, codes, values, i + 1);
        }
    }
}

int checkInstructionAcc(bool * instructions, string * codes, int* values, int i, int accumulator) {
    if(i >= 626) {
        return accumulator;
    } else if(instructions[i] == 1) {
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

void zeros(bool * instructions) {
    for(int i = 0; i < 626; i++) {
        instructions[i] = 0;
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


    for(int i = 0; i < 626; i++) {
        if(codes[i] == "acc") {
            continue;
        } else if(codes[i] == "nop") {

            codes[i] = "jmp";

            if(checkInstruction(instructions, codes, values, 0)) {
                cout << i << endl;
                zeros(instructions);
                cout << checkInstructionAcc(instructions, codes, values, 0, 0) << endl;
            }

            zeros(instructions);

            codes[i] = "nop";

        } else {

            codes[i] = "nop";

            if(checkInstruction(instructions, codes, values, 0)) {
                cout << i << endl;
                zeros(instructions);
                cout << checkInstructionAcc(instructions, codes, values, 0, 0) << endl;
            }

            zeros(instructions);

            codes[i] = "jmp";
        }
    }

    return 0;
}