#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int calcSeatID(string boardingPass) {
    int l = 0;
    int r = 127;
    int s;
    for(int i = 0; i < 7; i++) {
        if(boardingPass[i] == 'F') {
            s = (l + r) / 2;
            r = s;
        } else {
            s = (l + r + 1) / 2;
            l = s;
        }
    }

    int row = l;

    l = 0;
    r = 7;
    for(int i = 7; i < 10; i++) {
        if(boardingPass[i] == 'L') {
            s = (l + r) / 2 ;
            r = s;
        } else {
            s = (l + r + 1) / 2;
            l = s;          
        }
    }

    int column = l;

    return row * 8 + column;

} 

bool plane[922];

int main() {

    ifstream file;
    file.open("input.txt");

    int max = 0;
    string boardingPass;
    int seatID;

    for(int i = 0; i < 875; i++) {
        file >> boardingPass;
        seatID = calcSeatID(boardingPass);
        plane[seatID] = true;
    }

    int i = 0;
    while(plane[i] == 0) {
        i++;
    }

    for(; i < 922; i++) {
        if(plane[i] == 0) {
            cout << i << endl;
            return 0;
        }
    }

    cout << max << endl;

    return 0;
}