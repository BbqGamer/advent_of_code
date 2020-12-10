#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

float distance(int x1, int y1, int x2, int y2) 
{ 
    return sqrt(pow(x2 - x1, 2) +  
                pow(y2 - y1, 2) * 1.0); 
} 

int numbersOfPoints[2500];

int main() {

    ifstream file;
    file.open("dane.txt");

    int x[2500];
    int y[2500];

    for(int i = 0; i < 2500; i++) {
        file >> x[i];
        file >> y[i];
    }

    int dist;

    for(int i = 0; i < 2500; i++) {
        for(int j = 0; j < 2500; j++) {
            dist = distance(x[i], y[i], x[j], y[j]);
            if(dist <= 30 && i != j) {
                numbersOfPoints[i] += 1;
            }
        }
    }

    int max = 0;
    int maxI;
    for(int i = 0; i < 2500; i++) {
        if(numbersOfPoints[i] > max) {
            maxI = i;
            max = numbersOfPoints[i];
        }
    }

    cout << x[maxI];

    return 0;
}