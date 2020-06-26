bool mycomp(pair<int,int>&a, pair<int,int>&b){
    return a.second<b.second;
}

int activitySelection(int start[], int end[], int n){
    vector<pair<int,int>> arr;
    for(int i=0;i<n;i++){
        arr.push_back(make_pair(start[i],end[i]));
    }
    sort(arr.begin(),arr.end(),mycomp);
    int x=0;
    int count =1;
    for(int i=1;i<n;i++){
        if(arr[x].second<=arr[i].first){
            x=i;
            count+=1;
        }
    }
    return(count);
}