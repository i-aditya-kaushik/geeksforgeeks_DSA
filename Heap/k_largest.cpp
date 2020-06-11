vector<int> kLargest(int arr[], int n, int k)
{
    priority_queue<int,vector<int>,greater<int>> q;
    vector<int> s;
    for(int i=0;i<n;i++){
        q.push(arr[i]);
    }
    for(int i=0;i<n-k;i++){
        q.pop();
    }
    while(q.size()!=0){
        s.push_back(q.top());
        q.pop();
    }
    reverse(s.begin(),s.end());
    return(s);
}