                                            >> TIME             >> iteration
merge:
INPUT:  temp, l, m, r
OUTPUT: merged sequence from l to r
    n1:= m-l+1                              >> 1                >> 1
    n2:= r-m                                >> 1                >> 1
    declare L[n1],R[n2] as temp array
    // copying data from l to n1 to L       >> n1-l             >> 1
    // copying data from m+1 to n2 to R     >> n2-m-1           >> 1
    i:=0,j:=0,k:=0                          >> 3                >> 1
    while i<n1 and j<n2                     >> 1                >> x + y
        if L[i]<=R[j]                       >> 3                >> x
            arr[k]:= L[i]
            i:=i+1
        else                                >> 3                >> y
            arr[k]:= R[j]
            j:=j+1
        k:=k+1                                 >> 1                >> x + y
    while i<n1                              >> 4                >> n1 - x
        arr[k]:=L[i]
        i:=i+1
        k:=k+1
    while j<n2                              >> 4                >> n2 - y
        arr[k]:=R[j]
        j:=j+1
        k:=k+1
    //end of merge
    Total                                   >> n1-l+n2-m-1+x+y+3x+3y+4n1-4x+4n2-4y
                                            ~~ O(r-l)
mergeSort:
INPUT: temp, l, r
OUTPUT: sorted sequence from l to r
    when l<r
    m:=(l+(r-1))/2
    mergeSort(temp, l, m)                   >> (m-l)log(m-l)    >> 1
    mergeSort(temp, m, r)                   >> (r-m)log(r-m)    >> 1
    merge(temp,l,(l+(r-1))/2,r)             >> r-l              >> 1
    //End of mergeSort
    Total                                   >> r-l + (m-l)log(m-l) + (r-m)log(r-m)
                                            ~~ O(nlog(n))
    //By masters theorm T(n)=2T(n/2)+n

sortMatrix: 
INPUT: matrix, n,m
OUTPUT: sorted matrix
    temp[n*m]
    //creating a single array of size n*m   >> n*m              >> 1
    i:=0,j:=0,k:=0
    for i<n
        for j<m
            temp[k]:=matrix[i][j]
            k:=k+1
            j:=j+1
        i:=i+1
    mergeSort(temp,0,temp_size-1)           >> n*mlog(mn)       >> 1
    //renewing the matrix                   >> n*m              >> 1

    //End of sortMatrix
    Total                                   >> n*m*(2+log(m*n))
                                            ~~ O(n*nlog(n))

sortedMatrixSearch:
INPUT: matrix,n,m,x
OUTPUT: location
    i:=0,j:=m-1
    while 0<i<n and 0<j<m
        if x=matrix[i][j]
            retrun (i,j)
        else if x<matrix[i][j]
            j:=j-1
        else
            i:=i+1
        if i=n
            i:=i-1
            j:=j+1
        if j=-1
            j:=m-1
            i:=i-1
    return -1,-1
    //End of main
    

main:
INPUT: matrix,n,m,x
OUTPUT: location of x
    sortMatrix(matrix,n,m)                  >> n*m*log(m*n)     >> 1
    sortedMatrixSearch(matrix,n,m,x)        >> n+m              >> 1
    //End of main
    Total                                   >> n*m * m + n
                                            ~~ O(n*nlog(n))
