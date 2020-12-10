#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int getTreesPerSlope(int x, int y, vector < string > input, int lineCount) {
    int xLength = input[0].length();
    int treeCount = 0; 
    int xPos = x;
    for(int yPos = y ; yPos < lineCount; yPos += y) {
        if(input[yPos][xPos%xLength] == '#') {
            treeCount += 1;
        }
        xPos += x;
    }
    return treeCount;
}

int main() {

    ifstream file;
    file.open("input.txt");

    vector< string > input;

    string line;
    int lineCount = 0;
    while(file >> line) {
        input.push_back(line);
        lineCount += 1;
    }

    file.close();

    /* task 1 */

    cout << getTreesPerSlope(3, 1, input, lineCount) << endl << endl;

    /* task 2 */

    
    long long wynik = getTreesPerSlope(1, 1, input, lineCount) * getTreesPerSlope(3, 1, input, lineCount);

    wynik *= getTreesPerSlope(5, 1, input, lineCount);
    wynik *= getTreesPerSlope(7, 1, input, lineCount);
    wynik *= getTreesPerSlope(1, 2, input, lineCount);


    cout << wynik;

    return 0;
}