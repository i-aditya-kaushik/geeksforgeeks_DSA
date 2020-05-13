int subArraySum(int arr[], int n, int sum)
{
    unordered_map<int, int> prevSum; 
    int res = 0; 
    int currsum = 0; 
    for (int i = 0; i < n; i++) { 
        currsum += arr[i]; 
        if (currsum == sum)  
            res++;         
        if (prevSum.find(currsum - sum) !=  prevSum.end())  
            res += (prevSum[currsum - sum]); 
        prevSum[currsum]++; 
    } 
  
    return res; 
}