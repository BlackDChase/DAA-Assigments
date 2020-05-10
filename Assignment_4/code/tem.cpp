#include<bits/stdc++.h>
using namespace std;

#define MAX 100 

void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 
  
    /* create temp arrays */
    int L[n1], R[n2]; 
  
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
  
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray 
    j = 0; // Initial index of second subarray 
    k = l; // Initial index of merged subarray 
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
  
    /* Copy the remaining elements of L[], if there 
       are any */
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    /* Copy the remaining elements of R[], if there 
       are any */
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if (l < r) 
    { 
        // Same as (l+r)/2, but avoids overflow for 
        // large l and h 
        int m = l+(r-l)/2; 
  
        // Sort first and second halves 
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
} 
 
void binarySearch(int mat[][MAX], int i, int j_low,int j_high, int x) 
{ 
  while (j_low <= j_high) 
  { 
    int j_mid = (j_low + j_high) / 2; 

    if (mat[i][j_mid] == x) 
    { 
      cout << "Found at (" << i << ", "<< j_mid << ")"; 
      return; 
    } 
    else if (mat[i][j_mid] > x) 
        j_high = j_mid - 1; 
    else
        j_low = j_mid + 1; 
  } 
  cout << "Element no found"; 
} 

void sortedMatrixSearch(int mat[][MAX], int n,int m, int x) 
{ 

    if (n == 1) 
    { 
        binarySearch(mat, 0, 0, m-1, x); 
        return; 
    } 

    int i_low = 0; 
    int i_high = n-1; 
    int j_mid = m/2;

    while ((i_low+1) < i_high) 
    { 
        int i_mid = (i_low + i_high) / 2; 

        if (mat[i_mid][j_mid] == x) 
        { 
            cout << "Found at (" << i_mid << ", "<< j_mid << ")"; 
            return; 
        } 
        else if (mat[i_mid][j_mid] > x) 
            i_high = i_mid; 
        else
            i_low = i_mid;
    } 

    if (mat[i_low][j_mid] == x) 
        cout << "Found at (" << i_low << ","<< j_mid << ")"; 
    else if (mat[i_low+1][j_mid] == x) 
        cout << "Found at (" << (i_low+1)<< ", " << j_mid << ")"; 
    else if (x <= mat[i_low][j_mid-1]) 
        binarySearch(mat, i_low, 0, j_mid-1, x); 
    else if (x >= mat[i_low][j_mid+1]  && x <= mat[i_low][m-1]) 
       binarySearch(mat, i_low, j_mid+1, m-1, x); 
    else if (x <= mat[i_low+1][j_mid-1]) 
        binarySearch(mat, i_low+1, 0, j_mid-1, x); 
    else
        binarySearch(mat, i_low+1, j_mid+1, m-1, x); 
} 
  
void sortMatrix(int matrix[MAX][MAX], int n, int m){
    int temp[n*m], s = 0; 
   
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < m; j++, s++) 
            temp[s] = matrix[i][j]; 
   
    int temp_size = sizeof(temp)/sizeof(temp[0]);
    mergeSort(temp, 0, temp_size - 1); 
      
    s = 0; 
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < m; j++, s++) 
            matrix[i][j] = temp[s]; 
} 

int main() 
{ 
    int matrix[MAX][MAX], n, m;

    cout<<"Enter the size of row: ";
    cin>>n;
    cout<<"Enter the size of column: ";
    cin>>m;

    cout<<"\nInput the elements of matrix: \n";
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            cin>>matrix[i][j];
    
    sortMatrix(matrix, n, m); 
  
    cout << "\nMatrix After Sorting:\n"; 
    for (int i = 0; i < n; i++) { 
        for (int j = 0; j < m; j++) 
            cout << matrix[i][j] << " "; 
        cout << endl; 
    }

    int x;
    cout << "Enter Element to search:\n";
    cin >> x;
    sortedMatrixSearch(matrix, n, m, x);
      
    return 0; 
}
