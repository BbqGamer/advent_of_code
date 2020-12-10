#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int transformToSys(int decNumber, int system) {
    int newNumber = 0;
    int i = 0;
    while(decNumber > 0) {
        newNumber += (decNumber % system) * pow(10, i);
        i += 1;
        decNumber /= system;
    }
    return newNumber;
}

int transformToDec(int number, int system) {
    int decNumber = 0;
    int i = 0;
    while(number > 0) {
        decNumber += (number % 10) * pow(system, i);
        i += 1;
        number /= 10;
    }
    return decNumber;
}

int digitSum(int number) {
    int sum = 0;
    while(number > 0) {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}

bool isBigger(int first, int second) {

    if(digitSum(first) > digitSum(second)) {
        return true;
    } else if (digitSum(first) < digitSum(second)) {
        return false;
    } else {
        for(int i = 9; i >= 2; i--) {
            first = transformToDec(first, i + 1);
            second = transformToDec(second, i + 1);
            first = transformToSys(first, i);
            second = transformToSys(second, i);

            if(digitSum(first) > digitSum(second)) {
                return true;
            } else if (digitSum(first) < digitSum(second)) {
                return false;
            }
        }
    }
    return true;
}

int main() {

    ifstream file;
    file.open("input.txt");

    long number;
    int max = 1000;

    for(int i = 0; i < 10000; i++) {
        file >> number;
        if(isBigger(number, max)) {
            max = number;
        }
    }

    cout << max;

    return 0;
}