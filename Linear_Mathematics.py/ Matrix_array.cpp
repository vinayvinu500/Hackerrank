# https://www.hackerrank.com/challenges/linear-algebra-foundations-4-matrix-multiplication/problem?isFullScreen=true
#include <iostream>
using namespace std;

const int n = 3;

// Dynamic array => creating an array
int** matrix(){
    int** arr = new int*[n];
    for (int i=0;i<n;i++){
        arr[i] = new int[n];
        for (int j=0;j<n;j++){
            arr[i][j] = 0;
        }
    }
    return arr;
}

// printing an array
void print(int** arr){
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            cout << arr[i][j] << ' ';
        }
        cout << endl;
    }
}

// multiply two array = insert into new array
int** power(int* a){
    int **arr;
    arr = matrix();

    // input array representation
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            cout << a[i] << ' ';
        }
        cout << endl;
    }
    cout << endl;

    // modifiying array
    int op = 0;
    for (int i=0; i<n;i++){
        for (int k=0; k<n; k++){
            for (int j=0; j<n; j++){
                // cout << a[i][j];
                // op += a[i][j] * a[j][k];
                op++;
            }
            arr[i][k] = op;
            op = 0; 
        }
    }
    return arr;
}

int main() {
    int a[3][3] = {
        {1,1,0},
        {0,1,0},
        {0,0,1}
    };

    int **ar;
    ar = power(*a);
    print(ar);
    return 0;
}

