int *mergeKArrays(int arr[][N], int k)
{
    int* output;
    output = new int[k*k];
    int c=0; 
    for(int i=0; i<k; i++) 
    { 
        for(int j=0; j<k ;j++) 
            output[c++]=arr[i][j]; 
    } 
    sort(output,output + k*k); 
    return(output);
}