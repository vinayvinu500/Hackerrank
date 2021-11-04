#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

/*
    matrix = [2][2]
      A      B
    [1,2]  [4,5]
    [2,3]  [7,8]

    multiplication = row x col

    # first left => 1x4 + 2x7 = 4+14 = 18
    step 1: [0][0] x [0][0]
    Addition (+)
    step 2: [0][1] x [1][0]
    
    # first right => 1x5 + 2x8 = 5+16 = 21
    step 1: [0][0] x [0][1]
    Addition (+)
    step 2: [0][1] x [1][1]

    # second left => 2x4 + 3x7 = 8+21 = 29
    step 1: [1][0] x [0][0]
    Addition (+)
    step 2: [1][1] x [1][0]
    
    # second right => 2x5 + 3x8 = 10+24 = 34
    step 1: [1][0] x [0][1]
    Addition (+)
    step 2: [1][1] x [1][1]

    # understanding
    [0][0] [0][0] ==> 00 00
    [0][1] [1][0] ==> 01 10

    [0][0] [0][1] ==> 00 01
    [0][1] [1][1] ==> 01 11

    [1][0] [0][0] ==> 10 00
    [1][1] [1][0] ==> 11 10

    [1][0] [0][1] ==> 10 01
    [1][1] [1][1] ==> 11 11


    */
    

int main() {
    // matrix 2x2
    // int a[2][2] = {
    //     {1,2},
    //     {2,3}
    // };
    // int b[2][2] = {
    //     {4,5},
    //     {7,8}
    // };

    // matrix 3x3
    // int a[3][3] = {
    //     {1,2,3},
    //     {4,5,6},
    //     {7,8,9}
    // };

    // int b[3][3] = {
    //     {9,8,7},
    //     {6,5,4},
    //     {3,2,1}
    // };

    int a[3][3] = {
        {1,2,3},
        {2,3,4},
        {1,1,1}
    };
    
    int b[3][3] = {
        {4,5,6},
        {7,8,9},
        {4,5,7}
    };

    // loop method
    int m = sqrt(sizeof(a)/sizeof(a[0][0])); // matrix size of row or col
    vector <int> re;
    int op = 0;
    int br = 0;

    for (int i=0; i<m;i++){
        for (int k=0; k<m; k++){
            for (int j=0; j<m; j++){
                // cout << i << j << j << k << endl;
                // cout << a[i][j] << b[j][k] << endl;
                op += a[i][j] * b[j][k];
            }
            re.push_back(op);

            cout << op;
            if (br != m*m-1){
                cout << ',' << ' ';
            }
            op = 0;
            br ++;
            // cout << ' ' << endl;
        }
    }
    return 0;
}