vector <int> nearlySorted(int arr[], int num, int K){
    vector<int> q;
    priority_queue<int,vector<int>,greater<int>> s;
    for(int i=0;i<num;i++){
        s.push(arr[i]);
    }
    while(s.size()!=0){
        q.push_back(s.top());
        s.pop();
    }
    return(q);
}