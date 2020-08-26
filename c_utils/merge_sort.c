/* l is for left index and r is right index of the
   sub-array of arr to be sorted */


void merge_sort(int array[], int l, int r){
    if (l < r){
        int m = l+(r-l)/2;
        merge_sort(array, l, m);
        merge_sort(array, m+1, r);
        merge(array, l, m, r);
    }
}


void merge(int array[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++)
        L[i] = array[l + i];
    for (j = 0; j < n2; j++)
        R[j] = array[m + 1+ j];
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2){
        if (L[i] <= R[j]){
            array[k] = L[i];
            i++;
        }
        else{
            array[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1){
        array[k] = L[i];
        i++;
        k++;
    }
    while (j < n2){
        array[k] = R[j];
        j++;
        k++;
    }
}
