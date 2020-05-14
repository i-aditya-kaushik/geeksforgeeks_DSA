long long int countSubarrWithEqualZeroAndOne(int arr[], int n)
{
    for(int i =0;i<n;i++){
        if(arr[i]==0){
            arr[i]=-1;
        }
    }
    int sum=0,count=0;
    unordered_map<int,int>s;
    s[0]++;
    for(int i=0;i<n;i++){
        sum+=arr[i];
        if(s.find(sum)!=s.end()){
                count+=s[sum];
            }
        s[sum]++;
    }
    return count;
    
}