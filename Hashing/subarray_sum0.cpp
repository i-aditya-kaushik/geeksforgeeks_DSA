bool subArrayExists(int arr[], int n)
{
    int sum =0;
    unordered_set <int> s;
    for(int i=0;i<n;i++){
        sum+=arr[i];
        if(sum==0){
            return(1);
        }
        if(s.find(sum)!=s.end()){
            return(1);
        }
        s.insert(sum);
    }
    return(0);
}