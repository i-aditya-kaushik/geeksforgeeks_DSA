int kthSmallest(int arr[], int n, int k){
    sort(arr,arr+n);
    return(arr[k-1]);
} 

//NOTE: The priority queue program was not accepted
