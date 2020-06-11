int KthLargest(int arr[], int n, int k) {
    sort(arr,arr+n,greater<int>());
    return(arr[k-1]);
}