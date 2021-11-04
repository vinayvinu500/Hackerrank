# https://www.hackerrank.com/challenges/linear-algebra-foundations-5-the-100th-power-of-a-matrix/problem?h_r=internal-search
# include <iostream>
# include <cmath>
using namespace std;

constexpr int M = 3;

int matrix_multiple(int a[][M]){

    int arr[M][M] = {
        {0,0,0},
        {0,0,0},
        {0,0,0}
    };

    int m = M; // sqrt(sizeof(a)/sizeof(a[0][0])); // matrix size of row or col
    int op = 0;
    

    for (int i=0; i<m;i++){
        for (int k=0; k<m; k++){
            for (int j=0; j<m; j++){
                op += a[i][j] * a[j][k];
            }
            // *a[i][k] = op;
            arr[i][k] = op;
            cout << op << ' ';
            op = 0; 
        }
        cout << endl;
    }
    return arr[m][m];
}

int main(){

    int a[M][M] = {
        {1,1,0},
        {0,1,0},
        {0,0,1}
    };

    for (int i=0;i<50;i++){
        cout << matrix_multiple(a);
        break;
        
    }
    
    return 0;
}